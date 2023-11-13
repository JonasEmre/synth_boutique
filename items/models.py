from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(
        upload_to='brand_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True)
    is_sold = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    images = models.ImageField(
        upload_to='product_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
