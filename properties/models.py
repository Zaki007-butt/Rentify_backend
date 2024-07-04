from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class PropertyCategory(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class PropertyType(models.Model):
  category = models.ForeignKey(
    PropertyCategory, 
    on_delete=models.CASCADE, 
    related_name='types'
  )
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Property(models.Model):
  STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive')
  )

  title = models.CharField(
    max_length=200,
    validators=[MaxLengthValidator(200)],
    blank=False,
    null=False
  )
  description = models.TextField(
    blank=False,
    null=False
  )
  price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0.01)],
    blank=False,
    null=False
  )
  address = models.CharField(
    max_length=255,
    validators=[MaxLengthValidator(255)],
    blank=False,
    null=False
  )
  status = models.CharField(
    max_length=30,
    choices=STATUS_CHOICES,
    default='active'
  )
  property_category = models.ForeignKey(
    PropertyCategory,
    on_delete=models.SET_NULL,
    related_name='properties',
    blank=True,
    null=True
  )
  property_type = models.ForeignKey(
    PropertyType,
    on_delete=models.SET_NULL,
    related_name='properties',
    blank=True,
    null=True
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
