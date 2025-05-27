from django.db import models
from django.contrib.auth.models import User


# Секоја недвижност која може да се огласи за продавање се карактеризира со име,
# опис на локацијата каде се наоѓа, површина која ја зафаќа, датум кога е објавена за продавање,
# фотографија, информација дали некој ја резервирал и информација дали е веќе можеби продадена.

class Property(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    date_released = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    is_reserved = models.BooleanField(default=False, blank=True, null=True)
    is_sold = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_full_price(self):
        total_price = 0
        for prop_char in PropertyCharacteristics.objects.filter(property_id=self.id).all():
            total_price += prop_char.characteristic.price

        return total_price

    def get_all_characteristics(self):
        str_chars = ''
        for prop_char in PropertyCharacteristics.objects.filter(property_id=self.id).all():
            str_chars += prop_char.characteristic.name
            str_chars += ','

        return str_chars[:-1]


# Агентите кои се задолжени за продажба во агенцијата се карактеризираат со име и презиме,
# телефон за контакт, линк до нивен профил од LinkedIn,
# број на извршени продажби до сега и email адреса.

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    sold_properties = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class PropertyAgent(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.agent} sells {self.property}'


class Characteristic(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class PropertyCharacteristics(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Property: {self.property} has characteristic: {self.characteristic}'
