from django.shortcuts import render
from rest_framework import status, viewsets, mixins, generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from fipe.serializers import FipeSerializer
from fipe.service import consult

class FipeViewSet(viewsets.ViewSet,mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        "Busca Fipe Placa"
        serializer = FipeSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            response = consult(validated_data['plate'],validated_data['vehicle_type'])
            return Response(response)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
