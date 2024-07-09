from .views import Supplierviewset, SupplierOrderviewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'suppliers', Supplierviewset)
router.register(r'supplier-orders', SupplierOrderviewset)

urlpatterns = [
    path('', include(router.urls)),
]



