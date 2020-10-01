from rest_framework import serializers
from quotation import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'


class VehicleSpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleSpecie
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = '__all__'


class ChosenPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChosenPlan
        fields = '__all__'
