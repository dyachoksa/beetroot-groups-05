from django.shortcuts import render

from books.models import Book


def home(request):
    latest_books = Book.objects.order_by('-created_at')[:3]

    context = {
        "latest_books": latest_books,
    }

    return render(request, "home.html", context=context)


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms.html")
