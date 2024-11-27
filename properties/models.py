from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from account.models import User
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


class Customer(models.Model):
  user = models.ForeignKey(
    'account.User',
    on_delete=models.CASCADE,
    related_name='customers'
  )

  cnic = models.CharField(
    max_length=15,
    unique=True,
    blank=False,
    null=False
  )
  phone_number = models.CharField(
    max_length=15,
    unique=True,
    blank=False,
    null=False
  )
  address = models.CharField(
    max_length=255,
    blank=False,
    null=False
  )

  class Meta:
    verbose_name_plural = "Customers"
    unique_together = ('user',)

  def __str__(self):
    return self.cnic


class Agreement(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='agreements'
    )

    customer = models.ForeignKey(
      Customer,
      on_delete=models.CASCADE,
      related_name='agreements',
    )

    customer_note = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='agreements/',
        blank=True,
        null=True
    )
    details = models.TextField(
        blank=True,
        null=True
    )
    rent_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    rent_start_date = models.DateField(
        blank=True,
        null=True
    )
    rent_end_date = models.DateField(
        blank=True,
        null=True
    )
    purchase_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    purchase_date = models.DateField(
        blank=True,
        null=True
    )
    security_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Agreements"

    def __str__(self):
        return f"Agreement for {self.property.title}"

