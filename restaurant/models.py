from django.db import models

class Booking(models.Model):
    name = models.TextField(null=True)
    no_of_guests = models.IntegerField(null=True)
    bookingDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.TextField(null=True)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    inventory = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title
