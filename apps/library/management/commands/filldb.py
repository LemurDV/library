from django.core.management.base import BaseCommand
from loguru import logger

from apps.library.models import BookAuthor, Book, PublishingHouse, PublishingHouseView

names: list = ["Вася", "Оля", "Петя", "Галя", "Ваня", "Маша", "Олег", "Катя", "Илья", "Таня", "Жмых"]
s_names: list = ["Нсков", "Пыпа", "Гига", "Дуля", "Ожвых", "Крыля", "Сасян", "Хуятя", "Молодец", "Молодецева", "Пып"]
t_names: list = [
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
    "Петрович",
]
books_names: list = [
    "Прощай, оружие!",
    "Пикник у обочины",
    "Мартин Иден",
    "Цветы",
    "Ночной позор",
    "Грязь",
    "Лучше бы его не было",
    "Фиеста",
    "Война и мир",
    "Танатонавты",
    "Жмых",
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_books_author()
        fill_publishing_houses()
        fill_books()
        fill_publishing_houses_view()


def fill_books_author():
    bulk_objects = [
        BookAuthor(name=name, s_name=s_name, t_name=t_name)
        for name, s_name, t_name in zip(names, s_names, t_names)
    ]
    BookAuthor.objects.bulk_create(objs=bulk_objects)
    logger.success("Books authors was successfully created")


def fill_publishing_houses():
    bulk_objects = [PublishingHouse(name=f"Publishing House {i}") for i in range(1, len(s_names))]
    PublishingHouse.objects.bulk_create(objs=bulk_objects)
    logger.success("Publishing Houses was successfully created")


def fill_books():
    bulk_objects = []
    for book_name, author, p_house in zip(books_names, BookAuthor.objects.all(), PublishingHouse.objects.all()):  # type: str, BookAuthor, PublishingHouse
        bulk_objects.append(Book(name=book_name, author=author, publishing_house=p_house))
    Book.objects.bulk_create(objs=bulk_objects)
    logger.success("Employees was successfully created")


def fill_publishing_houses_view():
    bulk_objects = []
    for p_house, book in zip(PublishingHouse.objects.all(), Book.objects.all()):
        bulk_objects.append(PublishingHouseView(p_house=p_house, books=book))
    PublishingHouseView.objects.bulk_create(objs=bulk_objects)
    logger.success("Publishing Houses views was successfully created")
