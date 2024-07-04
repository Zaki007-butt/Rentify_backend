from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Property
from .serializers import PropertySerializer

class PropertyPagination(PageNumberPagination):
  page_size = 12
  page_size_query_param = 'page_size'
  max_page_size = 100

class PropertyViewSet(viewsets.ModelViewSet):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  filter_backends = [filters.OrderingFilter]
  ordering_fields = ['created_at']
  pagination_class = PropertyPagination

  def get_queryset(self):
    queryset = Property.objects.all()
    category_id = self.request.query_params.get('category_id')
    type_id = self.request.query_params.get('type_id')

    if category_id:
      queryset = queryset.filter(property_category_id=category_id)
    if type_id:
      queryset = queryset.filter(property_type_id=type_id)
    
    queryset = queryset.order_by('-created_at')
    return queryset
