from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, mixins, filters
from quotation import serializers
from quotation import models
from django_filters.rest_framework import DjangoFilterBackend


class PersonViewSet(viewsets.ModelViewSet):
    """Gerencia pessoas no banco"""
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class PlanViewSet(viewsets.ModelViewSet):
    """Gerencia planos no banco"""
    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()
    filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle_specie__id', 'vehicle_type__id']


class VehicleViewSet(viewsets.ModelViewSet):
    """Gerencia veículos no banco"""
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()


class VehicleSpecieViewSet(viewsets.ModelViewSet):
    """Gerencia espécies de veículos no banco"""
    serializer_class = serializers.VehicleSpecieSerializer
    queryset = models.VehicleSpecie.objects.all()
    filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle_type__id']


class VehicleTypeViewSet(viewsets.ModelViewSet):
    """Gerencia tipos de veículos no banco"""
    serializer_class = serializers.VehicleTypeSerializer
    queryset = models.VehicleType.objects.all()


class ChosenPlanViewSet(viewsets.ModelViewSet):
    """Gerencia Planos escolhidos no banco"""
    serializer_class = serializers.ChosenPlanSerializer
    queryset = models.ChosenPlan.objects.all()

