from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class PropertyCategory(models.Model):
  name = models.CharField(max_length=100, unique=True)

  class Meta:
      verbose_name_plural = "Property Categories"

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

  RENT_OR_BUY_CHOICES = (
    ('rent', 'Rent'),
    ('buy', 'Buy')
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
  price = models.TextField(
     blank=False,
    null=False
   # max_digits=10,
   # decimal_places=2,
    #validators=[MinValueValidator(0.01)],
    #blank=False,
    #null=False
  )
  address = models.CharField(
    max_length=255,
    validators=[MaxLengthValidator(255)],
    blank=False,
    null=False
  )
  city = models.CharField(
    max_length=100,
    validators=[MaxLengthValidator(100)],
    blank=False,
    null=False,
    default='Sialkot'
  )
  status = models.CharField(
    max_length=30,
    choices=STATUS_CHOICES,
    default='active'
  )
  bedroom = models.IntegerField(
    validators=[MinValueValidator(0)],
    blank=True,
    null=True
  )
  washroom = models.IntegerField(
    validators=[MinValueValidator(0)],
    blank=True,
    null=True
  )
  area = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0)],
    blank=True,
    null=True
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
  rent_or_buy = models.CharField(
    max_length=10,
    choices=RENT_OR_BUY_CHOICES,
    default='buy'
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  class Meta:
    verbose_name_plural = "Properties"

  def __str__(self):
    return self.title
