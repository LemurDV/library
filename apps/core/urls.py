from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.library.views import ModelAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/export", TemplateView.as_view(template_name="some.html"), name="export"),
    path("model", ModelAPIView.as_view(), name="model"),
]
