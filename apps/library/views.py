from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.models import Book
from apps.library.components.abstract_model_manager import AbstractModelManager


class BooksAPIView(APIView):
    def get(self, request) -> Response:
        books = Book.objects.all()
        context = {
            "books": books,
            "model": [
                f.name
                for f in Book._meta.get_fields()
                if not f.auto_created or f.one_to_one or (f.many_to_one and f.related_model)
            ]
        }

        return render(request, 'get_books.html', context)


class ExportModelAPIView(APIView):
    def post(self, request: Request) -> Response:
        AbstractModelManager().export_model(model_name=request.data.get("model"))
        return Response()
