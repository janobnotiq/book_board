from django.urls import path
from .views import BooksAPIView, HomePageView

urlpatterns = [
    path("books/",BooksAPIView.as_view()),
    path("home/",HomePageView.as_view()),
]
