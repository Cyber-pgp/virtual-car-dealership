from django.db import models



# Create your models here.
<<<<<<< HEAD

from django.db import models

class Car(models.Model):
    
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    miles = models.IntegerField()
    passengers = models.IntegerField()
    no_of_owners = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.color} {self.fuel_type}"
=======
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
>>>>>>> fa05d3787ffd17b5b3604c69c85c4db970af360f
