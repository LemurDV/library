from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.library.views import BooksAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/books", BooksAPIView.as_view(), name="books"),
    # path("model", ModelAPIView.as_view(), name="model"),
]
