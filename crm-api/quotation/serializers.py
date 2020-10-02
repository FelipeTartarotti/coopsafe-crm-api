from rest_framework import serializers
from quotation import models
from rest_framework.fields import SerializerMethodField

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


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


class PlanPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanPrice
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    price = SerializerMethodField()
    product = ProductSerializer(many=True)

    class Meta:
        model = models.Plan
        fields = '__all__'

    def get_price(self, obj):

        try:
            price = self.context['request'].query_params.get('vehicle_price')
            if not price:
                prices = models.PlanPrice.objects.filter(plan__id=obj.id)
                prices = PlanPriceSerializer(prices, many=True)
                return prices.data

            price = self.context['request'].query_params['vehicle_price'].replace(",",".")
            prices = models.PlanPrice.objects.filter(
                plan__id=obj.id,
                vehicle_price_from__lte=price,
                vehicle_price_to__gte=price
            )
            prices = PlanPriceSerializer(prices, many=True)
            return prices.data
        except:
            return []


class ChosenPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChosenPlan
        fields = '__all__'
