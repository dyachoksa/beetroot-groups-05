from datetime import timedelta

from operator import itemgetter
from django.db.models import Q, Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect
from django.utils import timezone

from books.models import Book, Category
from reviews.models import Review


def home(request):
    featured_books = Book.objects.filter(is_featured=True).order_by('-created_at')
    latest_books = Book.objects.select_related('author').order_by('-created_at')[:4]
    latest_reviews = Review.objects.select_related('book', 'user').order_by('-created_at')[:5]

    context = {
        "featured_books": featured_books,
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

def stats(request):
    ## Categories stats
    categories = Category.objects.annotate(num_books=Count("books")).order_by('name')

    # labels, data = [], []
    # for category in categories:
    #     labels.append(category.name)
    #     data.append(category.num_books)
    # or
    labels = [category.name for category in categories]
    data = [category.num_books for category in categories]

    categories_data = {
      "labels": labels,
      "datasets": [{
        "label": 'Number of books',
        "data": data,
        "hoverOffset": 4
      }]
    }

    ## Reviews stats
    reviews = Review.objects\
        .filter(created_at__gte=timezone.now() - timedelta(days=7))\
        .annotate(review_date=TruncDate("created_at"))\
        .values("review_date")\
        .annotate(num_reviews=Count("id"))\
        .order_by("review_date")
    
    reviews_data = {
        "labels": list(map(lambda x: x['review_date'].strftime('%b %d, %Y'), reviews)),
        "datasets": [{
            "label": "Number of reviews",
            "data": list(map(itemgetter('num_reviews'), reviews)),
            "tension": 0.3
        }]
    }

    context = {
        "categories_data": categories_data,
        "reviews_data": reviews_data,
    }

    return render(request, "stats.html", context=context)


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms.html")
