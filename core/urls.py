from django.urls import path
from .views import ProductListCreateView, OwnerListCreateView, PropertyListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('owners/', OwnerListCreateView.as_view(), name='owner-list-create'),
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
]
