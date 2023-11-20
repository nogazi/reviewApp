from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand_or_manufacturer = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    city_town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name