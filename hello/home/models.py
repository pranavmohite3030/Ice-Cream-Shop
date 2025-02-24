from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'
    
class IceCreamOrder(models.Model):
    icecream_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set when order is created

    def __str__(self):
        return f"{self.quantity} x {self.icecream_name}"    