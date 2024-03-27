from django.db import models
from datetime import datetime

# Create your models here.


class Product(models.Model):
    image = models.ImageField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=200)
    price = models.DecimalField(
        blank=False, null=False, max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_At = models.DateField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.Created_At
