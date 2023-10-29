from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Model


# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=30,blank=False, unique=True)
    description = models.CharField(max_length=120,blank=True)
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )