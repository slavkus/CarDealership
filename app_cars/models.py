from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=35)
    name = models.CharField(max_length=30)
    date_of_release = models.DateField()
    initial_price = models.IntegerField()


class Specifications(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    weight = models.IntegerField()
    seats = models.IntegerField()
    engine = models.CharField(max_length=20)
