"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books import views as book_views
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/<int:pk>/', book_views.author_detail, name="books_author"),
    path('books/<int:pk>/', book_views.book_detail, name="books_detail"),
    path('books/', book_views.book_list),
    path('about/', views.about, name="about"),
    path('terms/', views.terms, name="terms"),
    path('', views.home, name="index"),
]
