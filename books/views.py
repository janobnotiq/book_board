from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer


class BooksAPIView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class HomePageView(APIView):
    def get(self,request):
        count = Book.objects.count()
        return Response({"book_count": count,
                         "quote_count": 0,
                         "review_count": 0}, status=status.HTTP_200_OK)