from django.db import models

# Create your models here.

class ProductMain(models.Model):
    SIZE_CHOICES = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),)
    QUALITY_CHOICES = (
        ('high', 'high'),
        ('low', 'low'),
        ('medium', 'medium'),)
    Title = models.TextField(max_length=30)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    unique_code = models.IntegerField(unique=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    quality = models.CharField(max_length=6, choices=QUALITY_CHOICES)

class ProductColor(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('black', 'black'),)
    product = models.ForeignKey(ProductMain, on_delete=models.CASCADE , null=True,related_name="color")
    quality = models.CharField(max_length=5, choices=COLOR_CHOICES)

class productImage(models.Model):
    product = models.ForeignKey(ProductMain, on_delete=models.CASCADE , null=True,related_name="image")
    image = models.ImageField()

