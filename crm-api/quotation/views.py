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