from rest_framework import serializers

from .models import Category, Status, SubCategory, Transaction, Type


class StatusSerializer(serializers.ModelSerializer):
    """Cериализатор для статуса."""

    class Meta:
        model = Status
        fields = ["id", "name"]


class TypeSerializer(serializers.ModelSerializer):
    """Cериализатор для типа."""

    class Meta:
        model = Type
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    """Cериализатор для категории."""

    class Meta:
        model = Category
        fields = ["id", "name", "type"]


class SubCategorySerializer(serializers.ModelSerializer):
    """Cериализатор для подкатегории."""

    class Meta:
        model = SubCategory
        fields = ["id", "name", "category"]


class TransactionSerializer(serializers.ModelSerializer):
    """Cериализатор для подкатегории."""

    class Meta:
        model = Transaction
        fields = [
            "id",
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "description",
        ]
