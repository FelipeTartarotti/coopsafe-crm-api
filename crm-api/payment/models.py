from django.db import models

# Create your models here.


class Buyer(models.Model):

    buyer_id = models.CharField(max_length=200, null=True, blank=True)
    taxpayer_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.taxpayer_id)

    def retrieve_or_create(self, data):
        obj, created = Buyer.objects.get_or_create(
            taxpayer_id=data.get('cpf'),
            defaults={
                'taxpayer_id': data.get('cpf'),
            },
        )
        return obj


class CreditCard(models.Model):

    buyer = models.ForeignKey(Buyer, null=True, blank=True, on_delete=models.SET_NULL)
    card_number = models.CharField(max_length=200, null=True, blank=True)
    card_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.card_number)


class Shopping(models.Model):

    buyer = models.ForeignKey(Buyer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.card_number)