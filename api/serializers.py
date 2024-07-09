from rest_framework import serializers
from .models import Supplier, SupplierOrder


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrder
        fields = '__all__'
