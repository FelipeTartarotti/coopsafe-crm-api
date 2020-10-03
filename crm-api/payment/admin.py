from django.contrib import admin
from django.apps import	apps

payment = apps.get_app_config('payment')
# Register your models here.
for model_name, model in payment.models.items():
    admin.site.register(model)