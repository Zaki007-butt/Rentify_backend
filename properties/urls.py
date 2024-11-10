from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyCategoryViewSet, PropertyTypeViewSet, AgreementViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'categories', PropertyCategoryViewSet)
router.register(r'types', PropertyTypeViewSet)
router.register(r'agreements', AgreementViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
