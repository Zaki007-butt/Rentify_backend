from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PropertyViewSet, 
    PropertyCategoryViewSet, 
    PropertyTypeViewSet, 
    AgreementViewSet, 
    CustomerViewSet,
    PaymentViewSet
)

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'categories', PropertyCategoryViewSet)
router.register(r'types', PropertyTypeViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
