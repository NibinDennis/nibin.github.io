from django.db import models

# Create your models here.

class Flights(models.Model):
    name = models.CharField(max_length=100)
    flight_no = models.CharField(max_length=100)
    starting_from = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    food_supply = models.BooleanField()
    price = models.IntegerField()
    seats = models.IntegerField()
    status = models.CharField(max_length=100)