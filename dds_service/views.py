from django.shortcuts import get_object_or_404, redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from dds_service.models import Category, Status, SubCategory, Transaction, Type

from .filters import TransactionFilter
from .serializers import (CategorySerializer, StatusSerializer,
                          SubCategorySerializer, TransactionSerializer,
                          TypeSerializer)


# Статусы
class StatusView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_list.html"

    def get(self, request):
        queryset = Status.objects.all()
        return Response({"statuses": queryset})


class StatusDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_detail.html"

    def get(self, request, pk):
        queryset = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(queryset)
        return Response({"serializer": serializer, "obj": queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "obj": queryset})
        serializer.save()
        return redirect("/status/")


class StatusDestroyAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_delete.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({"obj": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("/status/")


class StatusCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "status_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/status/")
        else:
            return Response({"serializer": serializer})


# Типы
class TypeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_list.html"

    def get(self, request):
        queryset = Type.objects.all()
        return Response({"types": queryset})


class TypeDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_detail.html"

    def get(self, request, pk):
        queryset = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(queryset)
        return Response({"serializer": serializer, "obj": queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "obj": queryset})
        serializer.save()
        return redirect("/type/")


class TypeDestroyAPIView(generics.DestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_delete.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({"obj": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("/type/")


class TypeCreateAPIView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "type_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/type/")
        else:
            return Response({"serializer": serializer})


# Категории
class CategoryView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_list.html"

    def get(self, request):
        queryset = Category.objects.all()
        return Response({"categories": queryset})


class CategoryDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_detail.html"

    def get(self, request, pk):
        queryset = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(queryset)
        return Response({"serializer": serializer, "obj": queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "obj": queryset})
        serializer.save()
        return redirect("/category/")


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_delete.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({"obj": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("/category/")


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/category/")
        else:
            return Response({"serializer": serializer})


# Подкатегории
class SubCategoryView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_list.html"

    def get(self, request):
        queryset = SubCategory.objects.all()
        return Response({"subcategories": queryset})


class SubCategoryDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_detail.html"

    def get(self, request, pk):
        queryset = get_object_or_404(SubCategory, pk=pk)
        serializer = SubCategorySerializer(queryset)
        return Response({"serializer": serializer, "obj": queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(SubCategory, pk=pk)
        serializer = SubCategorySerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "obj": queryset})
        serializer.save()
        return redirect("/subcategory/")


class SubCategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_delete.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({"obj": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("/subcategory/")


class SubCategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "subcategory_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/subcategory/")
        else:
            return Response({"serializer": serializer})


# Движение денежных средств
class TransactionView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "transaction_list.html"
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get(self, request):
        queryset = Transaction.objects.all()
        filterset = TransactionFilter(request.GET, queryset=queryset)
        return Response({"transactions": filterset.qs})


class TransactionDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "transaction_detail.html"

    def get(self, request, pk):
        queryset = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(queryset)
        return Response({"serializer": serializer, "obj": queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "obj": queryset})
        serializer.save()
        return redirect("/transaction/")


class TransactionDestroyAPIView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "transaction_delete.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({"obj": obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect("/transaction/")


class TransactionCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "transaction_create.html"

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(
            {"serializer": serializer, "categories": Category.objects.all()}
        )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"serializer": serializer, "categories": Category.objects.all()},
                status=400,
            )

        serializer.save()
        return redirect("/transaction/")
