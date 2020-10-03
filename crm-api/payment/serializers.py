from rest_framework import serializers


class CreditCardSerializer(serializers.Serializer):

    cpf = serializers.CharField()
    holder_name = serializers.CharField()
    expiration_month = serializers.CharField()
    expiration_year = serializers.CharField()
    card_number = serializers.CharField()
    security_code = serializers.CharField()
    chosen_plan_id = serializers.IntegerField()
