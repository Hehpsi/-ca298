from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
   id = models.AutoField(primary_key=True)
   year = models.IntegerField()
   author = models.TextField()
   price = models.DecimalField(max_digits=5, decimal_places=2)
   title = models.TextField()
   synopsis = models.TextField()
   category = models.TextField(default="Horror")
   number = models.IntegerField()
   def __str__(self):
      return f"{self.title}"

class Customer(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.TextField(default="stranger")
   def __str__(self):
      return f"{self.name}"

class Borrow(models.Model):
   id = models.AutoField(primary_key=True)
   cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
   book = models.ForeignKey(Book, on_delete=models.CASCADE)
   is_returned = models.BooleanField(default=False)
   due_date = models.DateField(default=datetime.date.today)
   def __str__(self):
      return f"{self.cust.name} is borrowing {self.book.title}"
