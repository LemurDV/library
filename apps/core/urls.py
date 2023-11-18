from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.library.views import AuthorsAPIView, BooksAPIView, ExportModelAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/books", BooksAPIView.as_view(), name="books"),
    path("api/v1/authors", AuthorsAPIView.as_view(), name="authors"),
    path("api/v1/export-db", ExportModelAPIView.as_view(), name="export_db"),
]
