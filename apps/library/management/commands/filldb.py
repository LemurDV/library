from django.core.management.base import BaseCommand
from loguru import logger

from apps.library.models import BookAuthor, Book, PublishingHouse


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_managements()
        fill_departments()
        fill_employees()


def fill_managements():
    bulk_objects = [BookAuthor(name=f"Управление {i}") for i in range(1, 11)]
    BookAuthor.objects.bulk_create(objs=bulk_objects)
    logger.success("Managements was successfully created")


def fill_departments():
    bulk_objects = [PublishingHouse(name=f"Департамент {i}") for i in range(1, 11)]
    for i, obj in enumerate(bulk_objects, start=1):  # type: int, Department
        obj.management = BookAuthor.objects.filter(name=f"Управление {i}").get()

    PublishingHouse.objects.bulk_create(objs=bulk_objects)
    logger.success("Departments was successfully created")


def fill_employees():
    list_names = ["Вася", "Оля", "Петя", "Галя", "Ваня", "Маша", "Олег", "Катя", "Илья", "Таня"]
    bulk_objects = [Book(name=name, email=f"{name.lower()}@mail.ru") for name in list_names]
    for i, obj in enumerate(bulk_objects, start=1):
        obj.department = PublishingHouse.objects.filter(name=f"Департамент {i}").get()

    Book.objects.bulk_create(objs=bulk_objects)
    logger.success("Employees was successfully created")
