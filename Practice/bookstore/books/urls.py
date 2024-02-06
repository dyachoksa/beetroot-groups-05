from django.urls import path

from .views import author_detail, category_detail, book_detail, book_list


app_name = "books"

urlpatterns = [
    path('authors/<slug:slug>/', author_detail, name="author"),  # books:author
    path('by-category/<slug:slug>/', category_detail, name="category"),  # books:category
    path('<slug:slug>/', book_detail, name="detail"),  # books:details
    path('', book_list, name="list"),  # books:list
]
