from rest_framework import viewsets
from rest_framework import filters
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  filter_backends = [filters.OrderingFilter]
  ordering_fields = ['created_at']

  def get_queryset(self):
    queryset = Property.objects.all()
    category_id = self.request.query_params.get('category_id')
    type_id = self.request.query_params.get('type_id')

    if category_id:
      queryset = queryset.filter(property_category_id=category_id)
    if type_id:
      queryset = queryset.filter(property_type_id=type_id)

    return queryset
