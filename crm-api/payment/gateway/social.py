import base64
import json
import os
import requests
from app import settings
import uuid


def create_buyer_id(request,data):
    """Criar um id para o comprador"""

    path = os.path.join(settings.SOCIAL_URL,"buyers/")

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": settings.SOCIAL_TOKEN
    }

    data = {
        "name":data.get('holder_name'),
        "user_id":settings.SELLER_ID,
        "taxpayer_id": data.get('cpf')
    }

    request_result = requests.post(path, headers=headers, json=data)
    request_result_json = json.loads(request_result.text)

    return request_result_json.get("id")


def tokenize_card(request,data):
    """Cria token para o cartao"""

    path = os.path.join("https://api.zoop.ws/v1/marketplaces",settings.MARKETPLACE_ID,"cards/tokens")

    token = "".join([settings.ZPK,":",""])
    token = base64.b64encode(bytes(token, 'utf-8'))
    token = token.decode('ascii')

    headers = {
        "Content-Type": "application/json",
        "Authorization": "".join(["Basic ",token])
    }

    data = {
        "holder_name": data.get("holder_name"),
        "expiration_month": data.get("expiration_month"),
        "expiration_year":data.get("expiration_year"),
        "card_number":data.get("card_number"),
        "security_code":data.get("security_code"),
    }

    request_result = requests.post(path, headers=headers, json=data)
    request_result_json = json.loads(request_result.text)


    return request_result_json


def add_buyer_cards(tokenized_card,buyer_id,data):
    """Adiciona cartoes cadastrados do buyer"""

    path = os.path.join(settings.SOCIAL_URL,"cards","buyer")

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": settings.SOCIAL_TOKEN
    }

    body = {
        "buyer_id": buyer_id,
        "token": tokenized_card,
        "owner_taxpayer_id": data.get("cpf"),
        "description": "Coopsafe"
    }

    request_result = requests.post(path, headers=headers, json=body)
    request_result_json = json.loads(request_result.text)

    message = ""
    if request_result_json.get("detail"):
        message = request_result_json.get("detail")

    return {
        "message": message,
        "status_code": request_result.status_code,
        "id": request_result_json.get("id"),
    }


def make_payment(request,data,credit_card,chosen_plan):
    """Efetua o pagamento de crédito"""

    path = os.path.join(settings.SOCIAL_URL,"transactions/buyer")

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": settings.SOCIAL_TOKEN
    }

    adesao = chosen_plan.adesao.replace(".","")
    adesao = adesao.replace(",","")

    data = {
        "description": "".join(["Coopsafe", " - ", chosen_plan.plan.name]),
        "seller_id": settings.SELLER_ID,
        "buyer_id": credit_card.buyer.buyer_id,
        "reference_id":  uuid.uuid4().hex[:6].upper(),
        "card_id": credit_card.card_id,
        "amount": adesao,
    }


    request_result = requests.post(path, headers=headers, json=data)
    request_result_json = json.loads(request_result.text)

    if request_result.status_code != 200:

        return {"status_code":request_result.status_code,"message":request_result_json.get('message', "Erro ao efetuar pagamento")}

    return {"status_code":request_result.status_code,"detail":request_result_json}




