from django.db.models import Q
from django.shortcuts import render, redirect

from books.models import Book
from reviews.models import Review


def home(request):
    latest_books = Book.objects.select_related('author').order_by('-created_at')[:4]
    latest_reviews = Review.objects.select_related('book', 'user').order_by('-created_at')[:5]

    context = {
        "latest_books": latest_books,
        "latest_reviews": latest_reviews,
    }

    return render(request, "home.html", context=context)


def search(request):
    q = request.GET.get('q')
    if not q:
        return redirect('books_list')
    
    # We want to search in book title, book description, author name
    result = Book.objects.filter(
        Q(title__contains=q) | Q(description__contains=q) | Q(author__name__contains=q)
    ).select_related('author')[:10]

    context = {
        "q": q,
        "results": result
    }

    return render(request, "search_results.html", context=context)


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms.html")
