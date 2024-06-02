from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('dealer', 'Dealer'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    fuel = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    available = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
