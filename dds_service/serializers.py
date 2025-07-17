from rest_framework import serializers

from .models import Category, Status, SubCategory, Transaction, Type


class StatusSerializer(serializers.ModelSerializer):
    """Cериализатор для статуса."""

    class Meta:
        model = Status
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    """Cериализатор для типа."""

    class Meta:
        model = Type
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """Cериализатор для категории."""

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """Cериализатор для подкатегории."""

    class Meta:
        model = SubCategory
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    """Cериализатор для подкатегории."""

    class Meta:
        model = Transaction
        fields = "__all__"

    def validate(self, data):
        if data["subcategory"].category != data["category"]:
            raise serializers.ValidationError(
                "Данная подкатегория не связана с этой категорией!"
            )

        if data["category"].type != data["type"]:
            raise serializers.ValidationError(
                "Данная категория не связана с этим типом!"
            )

        return data
