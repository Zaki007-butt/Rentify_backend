from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyCategoryViewSet, PropertyTypeViewSet, AgreementViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'categories', PropertyCategoryViewSet)
router.register(r'types', PropertyTypeViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
