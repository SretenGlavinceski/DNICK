from django.db import models
from django.contrib.auth.models import User


# За секој производител се чува име, локација, краток опис,
# датум на основање и информација за тоа дали се во ЕУ или не.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date_founded = models.DateField()
    in_europe = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# производител, модел, тип на уред (мал, среден, голем),
# корисникот кој го креирал продуктот, фотографија од продуктот,
# цена, година на производство и информација за тоа дали е нов или не е

class Mobile(models.Model):
    TYPE_MOBILE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]
    mobile_model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type_mobile = models.CharField(max_length=1, choices=TYPE_MOBILE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mobiles/')
    price = models.IntegerField()
    year_manufactured = models.IntegerField()
    is_new = models.BooleanField(default=True)


    def __str__(self):
        return self.mobile_model
