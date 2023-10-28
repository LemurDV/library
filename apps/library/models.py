from django.db import models


class BookAuthor(models.Model):
    name = models.CharField(verbose_name="Book author name", max_length=20)
    s_name = models.CharField(verbose_name="Book author s_name", max_length=20)
    t_name = models.CharField(verbose_name="Book author t_name", max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.s_name} {str(self.name)[0]}. {str(self.t_name)[0]}."


class PublishingHouse(models.Model):
    name = models.CharField(verbose_name="Publishing House name", max_length=250, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(verbose_name="Book name", max_length=100)
    author = models.ForeignKey(to=BookAuthor, verbose_name="Book author", on_delete=models.CASCADE)
    publishing_house = models.OneToOneField(to=PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class PublishingHouseView(models.Model):
    p_house = models.ForeignKey(to=PublishingHouse, on_delete=models.CASCADE)
    books = models.ForeignKey(to=Book, verbose_name="Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.p_house.name
