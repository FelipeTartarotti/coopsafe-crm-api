from rest_framework import serializers

class FipeSerializer(serializers.Serializer):
    
    plate = serializers.CharField()
    vehicle_type = serializers.CharField()









