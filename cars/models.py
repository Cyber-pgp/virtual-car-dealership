from django.db import models
# Create your models here.

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

