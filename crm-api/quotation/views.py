from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, mixins
from quotation import serializers
from quotation import models


class PersonViewSet(viewsets.ModelViewSet):
    """Gerencia pessoas no banco"""
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class PlanViewSet(viewsets.ModelViewSet):
    """Gerencia planos no banco"""
    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    """Gerencia veículos no banco"""
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()


class VehicleSpecieViewSet(viewsets.ModelViewSet):
    """Gerencia espécies de veículos no banco"""
    serializer_class = serializers.VehicleSpecieSerializer
    queryset = models.VehicleSpecie.objects.all()


class ChosenPlanViewSet(viewsets.ModelViewSet):
    """Gerencia Planos escolhidos no banco"""
    serializer_class = serializers.ChosenPlanSerializer
    queryset = models.ChosenPlan.objects.all()