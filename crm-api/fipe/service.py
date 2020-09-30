import json
import os
import time

from app import settings
import requests


def post(url,body,header):
    "Requisicao post para PLACASFIPE"
    response = requests.post(url,json=body,headers=header)
    return json.loads(response.text)


def auth():
    "Autentica e busca o token na plataforma"
    header = {
        "Content-Type": "application/json"
    }
    path = os.path.join(settings.URL_PLACAS, "login")
    body = {
        "username": settings.PLATE_USER, "password": settings.PLATE_PASSWORD
    }

    return post(path,body,header)


def consult(plate,vehicle_type):
    "Consulta placa na plataforma"

    token = auth()
    header = {
        "Content-Type": "application/json",
        "Authorization": "".join(["JWT ",token['token']])
    }
    body = {
        "placa": plate,
        "tipo":  vehicle_type
    }
    path = os.path.join(settings.URL_PLACAS, "consulta")

    return post(path, body, header)




