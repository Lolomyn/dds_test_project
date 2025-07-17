from django.contrib import admin

from .models import Category, Status, SubCategory, Transaction, Type


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_filter = ("name", "type")
    search_fields = ("name", "type")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("name", "category")
    search_fields = ("name", "category")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "description",
    )
    list_filter = ("status", "type", "category", "amount")
    search_fields = ("category", "subcategory", "description")
