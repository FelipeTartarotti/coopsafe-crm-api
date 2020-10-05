from rest_framework import serializers
from payment import models
from quotation.serializers import ChosenPlanSerializer

class ShoppingSerializer(serializers.ModelSerializer):

    chosen_plan = ChosenPlanSerializer()

    class Meta:
        model = models.Shopping
        fields = '__all__'


class CreditCardSerializer(serializers.Serializer):

    cpf = serializers.CharField()
    holder_name = serializers.CharField()
    expiration_month = serializers.CharField()
    expiration_year = serializers.CharField()
    card_number = serializers.CharField()
    security_code = serializers.CharField()
    chosen_plan_id = serializers.IntegerField()
