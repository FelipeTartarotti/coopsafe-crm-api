from django.contrib import admin
from django.apps import	apps

quotation = apps.get_app_config('quotation')

for model_name, model in quotation.models.items():
    admin.site.register(model)