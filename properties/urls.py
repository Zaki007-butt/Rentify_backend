from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PropertyViewSet, 
    PropertyCategoryViewSet, 
    PropertyTypeViewSet, 
    AgreementViewSet, 
    CustomerViewSet,
    PaymentViewSet,
    UtilityBillViewSet,
    get_dashboard_stats
)

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'categories', PropertyCategoryViewSet)
router.register(r'types', PropertyTypeViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'utility-bills', UtilityBillViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('dashboard/stats/', get_dashboard_stats, name='dashboard-stats'),
]
