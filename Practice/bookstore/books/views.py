from django.shortcuts import render, get_object_or_404

from .models import Author, Book


def book_list(request):
    books = Book.objects.order_by('-created_at')

    context = {
        "books": books,
    }

    return render(request, "books/list.html", context=context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {
        "book": book,
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
