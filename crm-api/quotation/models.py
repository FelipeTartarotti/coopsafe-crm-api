from django.db import models

# Create your models here.

class VehicleType(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class VehicleSpecie(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class PlanPrices(models.Model):

    vehicle_price_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vehicle_price_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    plan_price = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)

    def __str__(self):
        return str(self.vehicle_price_from)


class Plan(models.Model):

    vehicle_type = models.ManyToManyField(VehicleType)
    vehicle_specie = models.ManyToManyField(VehicleSpecie)
    name = models.CharField(max_length=200, null=True, blank=True)
    plan_price = models.ManyToManyField(PlanPrices)

    def __str__(self):
        return str(self.name)


class Vehicle(models.Model):

    specie = models.CharField(max_length=200, null=True, blank=True)
    plate = models.CharField(max_length=200, null=True, blank=True)
    fipe_code = models.CharField(max_length=200, null=True, blank=True)
    vehicle_type = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    make = models.CharField(max_length=200, null=True, blank=True)
    fuel = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
            return str(self.plate)


class ChosenPlan(models.Model):

    plan_name = models.CharField(max_length=200, null=True, blank=True)
    adesao = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.plano)


class Person(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    chosen_plan = models.ForeignKey(ChosenPlan, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)

