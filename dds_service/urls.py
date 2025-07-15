from django.urls import include, path
from rest_framework.routers import DefaultRouter

from dds_service.apps import DdsServiceConfig

from .views import (CategoryCreateAPIView, CategoryDestroyAPIView,
                    CategoryDetailView, CategoryView, StatusCreateAPIView,
                    StatusDestroyAPIView, StatusDetailView, StatusView,
                    SubCategoryCreateAPIView, SubCategoryDestroyAPIView,
                    SubCategoryDetailView, SubCategoryView,
                    TransactionCreateAPIView, TransactionDestroyAPIView,
                    TransactionDetailView, TransactionView, TypeCreateAPIView,
                    TypeDestroyAPIView, TypeDetailView, TypeView)

router = DefaultRouter()

app_name = DdsServiceConfig.name

urlpatterns = [
    # статус
    path("status/", StatusView.as_view(), name="status"),
    path("status/<int:pk>/", StatusDetailView.as_view(), name="status-detail"),
    path(
        "status/<int:pk>/delete/", StatusDestroyAPIView.as_view(), name="status-delete"
    ),
    path("status/create/", StatusCreateAPIView.as_view(), name="status-create"),
    # тип
    path("type/", TypeView.as_view(), name="type"),
    path("type/<int:pk>/", TypeDetailView.as_view(), name="type-detail"),
    path("type/<int:pk>/delete/", TypeDestroyAPIView.as_view(), name="type-delete"),
    path("type/create/", TypeCreateAPIView.as_view(), name="type-create"),
    # категория
    path("category/", CategoryView.as_view(), name="category"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path(
        "category/<int:pk>/delete/",
        CategoryDestroyAPIView.as_view(),
        name="category-delete",
    ),
    path("category/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    # подкатегория
    path("subcategory/", SubCategoryView.as_view(), name="subcategory"),
    path(
        "subcategory/<int:pk>/",
        SubCategoryDetailView.as_view(),
        name="subcategory-detail",
    ),
    path(
        "subcategory/<int:pk>/delete/",
        SubCategoryDestroyAPIView.as_view(),
        name="subcategory-delete",
    ),
    path(
        "subcategory/create/",
        SubCategoryCreateAPIView.as_view(),
        name="subcategory-create",
    ),
    # транзакция
    path("transaction/", TransactionView.as_view(), name="transaction"),
    path(
        "transaction/<int:pk>/",
        TransactionDetailView.as_view(),
        name="transaction-detail",
    ),
    path(
        "transaction/<int:pk>/delete/",
        TransactionDestroyAPIView.as_view(),
        name="transaction-delete",
    ),
    path(
        "transaction/create/",
        TransactionCreateAPIView.as_view(),
        name="transaction-create",
    ),
]
