from django.db import models


class Status(models.Model):
    """Модель для хранений статусов."""

    name = models.CharField(max_length=128, unique=True, verbose_name="Статус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(models.Model):
    """Модель для хранений типов операций."""

    name = models.CharField(max_length=128, unique=True, verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Category(models.Model):
    """Модель для хранений категорий."""

    name = models.CharField(max_length=128, unique=True, verbose_name="Категория")
    type = models.ForeignKey(
        Type, on_delete=models.DO_NOTHING, verbose_name="Тип операции"
    )

    def __str__(self):
        return f"{self.type} | {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    """Модель для хранений подкатегорий."""

    name = models.CharField(max_length=128, unique=True, verbose_name="Подкатегория")
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.category}/{self.name}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Transaction(models.Model):
    """Модель для хранений движения денежных средств."""

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    status = models.ForeignKey(
        Status, on_delete=models.DO_NOTHING, verbose_name="Статус"
    )

    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name="Тип")

    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name="Категория"
    )

    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.DO_NOTHING, verbose_name="Подкатегория"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    description = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.status}/{self.created_at} - {self.amount} руб."

    class Meta:
        verbose_name = "Движение денежных средств"
        verbose_name_plural = "Движения денежных средств"
        ordering = ["-created_at"]
