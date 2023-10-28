from django.contrib import admin
from apps.library.models import BookAuthor, Book, PublishingHouse, PublishingHouseView


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "publishing_house"]

    # @staticmethod
    # def get_management_name(obj):
    #     return obj.management.name
    # get_management_name.short_description = "Управления"


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ["name", ]

    # @staticmethod
    # def get_department_name(obj):
    #     return obj.department.name
    # get_department_name.short_description = "Департаменты"
    #
    # @staticmethod
    # def get_management_name(obj):
    #     return obj.department.management.name
    # get_management_name.short_description = "Управления"


@admin.register(PublishingHouseView)
class PublishingHouseViewAdmin(admin.ModelAdmin):
    list_display = ["p_house", "books"]

    @staticmethod
    def _get_books(obj):
        return ", ".join(i for i in obj.books.objects.all())
