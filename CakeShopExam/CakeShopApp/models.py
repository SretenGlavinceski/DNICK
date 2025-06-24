from django.db import models
from django.contrib.auth.models import User


# Секој од овие корисници има име, презиме, телефон за контакт и email адреса.

class Baker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='bakers/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


# Секоја торта има име, цена, тежина, опис и слика.

class Cake(models.Model):
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cakes/', blank=True, null=True)

    def __str__(self):
        return self.name
