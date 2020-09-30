from django.shortcuts import render
from rest_framework import status, viewsets, mixins, generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from fipe.serializers import FipeSerializer
from fipe.service import consult
@authentication_classes([])
@permission_classes([])
class FipeViewSet(viewsets.ViewSet,mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        "Busca Fipe Placa"
        serializer = FipeSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            response = consult(validated_data['plate'],validated_data['vehicle_type'])
            return Response(response)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)




    # def login(self):

    #     header = {
    #         "Content-Type": "application/json"
    #     }

    #     body = {
    #         "username": settings.PLATE_USER, "password": settings.PLATE_PASSWORD
    #     }

    #     url = os.path.join(settings.URL_PLACAS, "login")

    #     response = requests.post(url, data=json.dumps(body), headers=header)

    #     response = json.loads(response.text)

    #     return response.get("token")

    # @action(methods=['post'], detail=False)
    # def consult(self, request):

    #     plate = request.data.get("plate")
    #     vehicle_type = request.data.get("vehicle_type")

    #     token = FipeViewSet.login(self)

    #     header = {
    #         "Content-Type": "application/json",
    #         "Authorization": "".join(["JWT ",token])
    #     }

    #     body = {
    #         "placa": plate,
    #         "tipo":  vehicle_type
    #     }

    #     url = os.path.join(settings.URL_PLACAS, "consulta")

    #     response = requests.post(url, data=json.dumps(body), headers=header)

    #     response = json.loads(response.text)

    #     if response.get("codigoRetorno") != '0':
    #         return HttpResponse(response, status=404)

    #     return Response(response)

    #     #carros, motos, caminhoes
