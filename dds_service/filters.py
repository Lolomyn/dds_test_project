import django_filters

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    date_to = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
    status__name = django_filters.CharFilter(
        field_name="status__name", lookup_expr="icontains"
    )
    category__name = django_filters.CharFilter(
        field_name="category__name", lookup_expr="icontains"
    )
    subcategory__name = django_filters.CharFilter(
        field_name="subcategory__name", lookup_expr="icontains"
    )

    class Meta:
        model = Transaction
        fields = [
            "date_from",
            "date_to",
            "status__name",
            "category__name",
            "subcategory__name",
        ]
