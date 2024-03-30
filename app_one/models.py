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
        return self.name

# have to refer and go through the types of fields ,enum field, choice field etc...

# class school_database(models.Model):
#     name = models.CharField(blank=False, null=False, max_length=200)
#     addres = models.TextField()
#     phone = models.CharField(blank=False, null=False, max_length=10)

#     def __str__(self) -> str:
#         return self.phone


# class vehicle_Data(models.Model):
#     vehicle_type = models.CharField(blank=False, null=False, max_length=50)
#     price = models.DecimalField(
#         blank=False, null=False, max_digits=5, decimal_places=2)
#     retest_Year = models.CharField(blank=False, null=False, max_length=4)

#     def __str__(self) -> str:
#         return self.vehicle_type
