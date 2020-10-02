from django.contrib import admin
from django.apps import	apps
from django.forms import CheckboxSelectMultiple
from quotation import models
quotation = apps.get_app_config('quotation')

class PlanPricesAdmin(admin.ModelAdmin):
    list_display = ('vehicle_price_from','vehicle_price_to',
                    'plan_price')

class PlanPriceInline(admin.StackedInline):
    model = models.PlanPrice
    extra = 0


class PlanAdmin(admin.ModelAdmin):
    inlines = [PlanPriceInline]
    save_as = True

    list_display = ('name','get_vehicle_type', 'get_vehicle_specie')

    def get_vehicle_type(self, obj):
        return "\n".join([p.name for p in obj.vehicle_type.all()])

    def get_vehicle_specie(self, obj):
        return "\n".join([p.name for p in obj.vehicle_specie.all()])

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'vehicle_type':
            kwargs['widget'] = CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        if db_field.name == 'vehicle_specie':
            kwargs['widget'] = CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        if db_field.name == 'product':
            kwargs['widget'] = CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        return db_field.formfield(**kwargs)


for model_name, model in quotation.models.items():
    if model_name == "planprices":
        admin.site.register(model,PlanPricesAdmin)
    elif model_name == "plan":
        admin.site.register(model,PlanAdmin)
    else:
        admin.site.register(model)