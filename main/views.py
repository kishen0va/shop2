from django.shortcuts import render

import django_filters.rest_framework
from rest_framework import viewsets, generics, mixins, filters
from .serializers import CategorySerializer, BrandSerializer, ClothersSerializer

from .models import Category, Brand, Clothes

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer 




class ClothersListViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filter_feileds = []
    search_fields = [('id', 'clothes_name', 'clothes_description', 'clothes_slug', 'clothes_type', 'clothes_season', 'clothes_price', 'clothes_image', 'clothes_brand', 'clothes_category', )]
    orderong_fields = ['id', 'clothes_name']