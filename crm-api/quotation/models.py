from django.db import models

# Create your models here.

class Vehicle(models.Model):

    specie = models.CharField(max_length=200, null=True, blank=True)
    plate = models.CharField(max_length=200, null=True, blank=True)
    fipe_code = models.CharField(max_length=200, null=True, blank=True)
    vehicle_type = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    make = models.CharField(max_length=200, null=True, blank=True)
    fuel = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
            return str(self.plate)


class Plan(models.Model):

    plano = models.CharField(max_length=200, null=True, blank=True)
    adesao = models.CharField(max_length=200, null=True, blank=True)
    total = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.plano)


class Person(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)

