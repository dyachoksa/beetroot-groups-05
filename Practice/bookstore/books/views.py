from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from reviews.forms import ReviewForm
from reviews.models import Review

from .models import Author, Book

books_per_page = 12
reviews_per_page = 10


def book_list(request):
    books = Book.objects.order_by('-created_at')
    paginator = Paginator(books, books_per_page)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "books": page_obj,
        "current_page": page_number
    }

    return render(request, "books/list.html", context=context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = Review()
            review.content = review_form.cleaned_data["content"]
            review.book = book
            review.user = request.user
            review.save()

            messages.success(request, "Your review has been added successfully.")

            return redirect("books_detail", book.pk)
    else:
        review_form = ReviewForm()

    reviews = book.reviews.order_by('-created_at')
    paginator = Paginator(reviews, reviews_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "book": book,
        "review_form": review_form,
        "reviews": page_obj,
    }

    return render(request, "books/detail.html", context=context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author).order_by('title')

    context = {
        "author": author,
        "books": books,
    }

    return render(request, "books/author.html", context=context)
