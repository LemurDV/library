from django.core.management.base import BaseCommand

from apps.library.models import BookAuthor, Book, PublishingHouse, PublishingHouseView


class Command(BaseCommand):
    def handle(self, *args, **options):
        BookAuthor.objects.all().delete()
        PublishingHouse.objects.all().delete()
        Book.objects.all().delete()
        PublishingHouseView.objects.all().delete()
