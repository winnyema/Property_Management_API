from django.shortcuts import render
from rest_framework import generics
from .models import Product, Owner, Property
from .serializers import ProductSerializer, OwnerSerializer, PropertySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


