from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    inventoryStatus = models.CharField(max_length=255, default="INSTOCK")
    category = models.CharField(max_length=255, default="Accessories")
    image = models.CharField(max_length=255, default="")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.code
