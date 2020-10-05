from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from payment import serializers
from payment.gateway import social
from payment import models
from quotation.models import ChosenPlan

class CreditCardViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        "Envia e-mails em massa"
        serializer = serializers.CreditCardSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:

                buyer = models.Buyer.retrieve_or_create(self, validated_data)
                if not buyer.buyer_id:
                    buyer.buyer_id = social.create_buyer_id(request, validated_data) #Cria Buyer
                    buyer.save()

                credit_card = models.CreditCard.retrieve_or_create(self, validated_data)
                if not credit_card.card_id:
                    tokenized_card = social.tokenize_card(request, validated_data) #Cria Token do cartao

                    buyer_cards = social.add_buyer_cards(tokenized_card.get('id'), buyer.buyer_id,
                                                         validated_data)  # Adiciona cartao ao buyer

                    if buyer_cards.get("status_code") != 200:
                        raise ValueError(buyer_cards.get("message"))

                    credit_card.card_id = buyer_cards.get('id')
                    credit_card.buyer_id = buyer.id
                    credit_card.save()

                chosen_plan = ChosenPlan.objects.get(id=validated_data.get('chosen_plan_id'))
                payment = social.make_payment(request, validated_data, credit_card, chosen_plan)

                if payment.get('status_code') == 200:
                    chosen_plan.status = 'PAID'
                    chosen_plan.save()

                return Response(payment)
            except Exception as error:

                return HttpResponse(error, status=400)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


