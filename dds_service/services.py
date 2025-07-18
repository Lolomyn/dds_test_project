from rest_framework import serializers


class TransactionService:

    @staticmethod
    def validate_subcategory(data):
        if data["subcategory"].category != data["category"]:
            raise serializers.ValidationError(
                "Данная подкатегория не связана с этой категорией!"
            )

    @staticmethod
    def validate_category(data):
        if data["category"].type != data["type"]:
            raise serializers.ValidationError(
                "Данная категория не связана с этим типом!"
            )
