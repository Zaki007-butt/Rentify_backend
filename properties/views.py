from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Property, PropertyCategory, PropertyType, Customer, Agreement
from .serializers import PropertySerializer, PropertyCategorySerializer, PropertyTypeSerializer, CustomerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import AgreementSerializer

class GeneralPagination(PageNumberPagination):
  page_size = 24
  page_size_query_param = 'page_size'
  max_page_size = 100000

class PropertyViewSet(viewsets.ModelViewSet):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  filter_backends = [filters.OrderingFilter, filters.SearchFilter]
  ordering_fields = ['created_at']
  search_fields = ['title', 'description', 'address']
  pagination_class = GeneralPagination

  def get_queryset(self):
    queryset = Property.objects.all()
    category_id = self.request.query_params.get('category_id')
    type_id = self.request.query_params.get('type_id')
    rent_or_buy = self.request.query_params.get('type')

    if category_id:
      queryset = queryset.filter(property_category_id=category_id)
    if type_id:
      queryset = queryset.filter(property_type_id=type_id)
    if rent_or_buy in ['rent', 'buy']:
      queryset = queryset.filter(rent_or_buy=rent_or_buy)
    
    queryset = queryset.order_by('-created_at')
    return queryset


class PropertyCategoryViewSet(viewsets.ModelViewSet):
  queryset = PropertyCategory.objects.all()
  serializer_class = PropertyCategorySerializer

  @action(detail=True, methods=['get'], url_path='types', url_name='property_types')
  def get_types(self, request, pk=None):
    category = self.get_object()
    property_types = PropertyType.objects.filter(category=category)
    serializer = PropertyTypeSerializer(property_types, many=True)
    return Response(serializer.data)

class PropertyTypeViewSet(viewsets.ModelViewSet):
  queryset = PropertyType.objects.all()
  serializer_class = PropertyTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  pagination_class = GeneralPagination

  @action(detail=False, methods=['get'], url_path='get', url_name='get_customer')
  def get_customer(self, request):
    user = request.user
    customer = Customer.objects.filter(user=user).first()  # Check if customer exists for the logged-in user
    if customer:
      serializer = self.get_serializer(customer)
      return Response({'customer': serializer.data}) 
    return Response({'customer': False})  # Return false if no customer is found
  
  @action(detail=False, methods=['get'], url_path='active_customers', url_name='active_customers')
  def get_active_customers(self, request):
    # Get all customers who have at least one agreement
    customers_with_agreements = Customer.objects.filter(
      agreements__isnull=False  # Ensure customer has at least one agreement
    ).distinct()
    
    serializer = self.get_serializer(customers_with_agreements, many=True)
    return Response({'results': serializer.data})


class AgreementViewSet(viewsets.ModelViewSet):
  def get_queryset(self):
    user = self.request.user
    if user.is_admin:
      return Agreement.objects.all().order_by('-created_at')
    else:
      return Agreement.objects.filter(customer__user=user).order_by('-created_at')

  queryset = Agreement.objects.all()
  serializer_class = AgreementSerializer
  pagination_class = GeneralPagination
