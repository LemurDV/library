from django.db import models


class BookAuthor(models.Model):
    name = models.CharField(verbose_name="Book author", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(verbose_name="Имя суслика", max_length=100)
    author = models.ForeignKey(to=BookAuthor, verbose_name="Book author", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PublishingHouse(models.Model):
    name = models.CharField(verbose_name="Publishing house name", max_length=250, unique=True)
    books = models.ForeignKey(to=Book, verbose_name="Book", on_delete=models.CASCADE, max_length=100)

    def __str__(self):
        return self.name
