from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SupplierOrder, Supplier
from .serializers import SupplierSerializer, SupplierOrderSerializer


class Supplierviewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierOrderviewset(viewsets.ModelViewSet):
    queryset = SupplierOrder.objects.all()
    serializer_class = SupplierOrderSerializer
