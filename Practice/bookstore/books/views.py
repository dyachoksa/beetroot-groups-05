from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect

from reviews.forms import ReviewForm
from reviews.models import Review

from .models import Author, Category, Book

books_per_page = 12
reviews_per_page = 10


def book_list(request):
    categories = Category.objects.all().order_by('name')

    books = Book.objects.select_related('author')

    sort_by = request.GET.get('sortBy', 'created_at')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'num_views':
        books = books.order_by('-num_views')
    else:
        books = books.order_by('-created_at')

    paginator = Paginator(books, books_per_page)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "books": page_obj,
        "current_page": page_number,
        "categories": categories,
        "sort_by": sort_by,
    }

    return render(request, "books/list.html", context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    books = category.books.select_related("author").order_by('-created_at')
    paginator = Paginator(books, books_per_page)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "books": page_obj,
    }

    return render(request, "books/category.html", context=context)


def book_detail(request, pk):
    Book.objects.filter(pk=pk).update(num_views=F("num_views") + 1)

    book_qs = Book.objects.select_related("author", "category")
    book = get_object_or_404(book_qs, pk=pk)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = Review()
            review.content = review_form.cleaned_data["content"]
            review.book = book
            review.user = request.user
            review.save()

            messages.success(request, "Your review has been added successfully.")

            return redirect(book)
    else:
        review_form = ReviewForm()

    reviews = book.reviews.select_related('user').order_by('-created_at')
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
    books = Book.objects.filter(author=author).select_related('author').order_by('title')

    context = {
        "author": author,
        "books": books,
    }

    return render(request, "books/author.html", context=context)
