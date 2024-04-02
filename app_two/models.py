from django.db import models

# Create your models here.


class student_doc(models.Model):
    name = models.CharField(blank=False, null=False, max_length=300)
    image = models.ImageField(blank=False, null=False)
    student_id = models.DecimalField(blank=False, null=False,
                                     max_digits=5, decimal_places=2)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name
