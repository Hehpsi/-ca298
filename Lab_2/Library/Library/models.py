from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.DateField()
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=50)
    synopsis = models.TextField()
