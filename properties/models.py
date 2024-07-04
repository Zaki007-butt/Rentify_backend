from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class Property(models.Model):
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
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
