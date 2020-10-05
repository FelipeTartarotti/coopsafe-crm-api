from django.contrib import admin
from django.apps import	apps
from django.forms import CheckboxSelectMultiple
from django.utils.html import format_html
from quotation import models
quotation = apps.get_app_config('quotation')

class ChosenPlanAdmin(admin.ModelAdmin):
    list_display = ('plan','get_person_name','get_person_whatsapp','get_person_email','adesao','get_status',)

    def get_person_name(self, obj):
        return "\n".join([obj.person.name])

    def get_person_whatsapp(self, obj):
        return "\n".join([obj.person.whatsapp])

    def get_person_email(self, obj):
        return "\n".join([obj.person.email])

    def get_status(self, obj):
        color = 'green'
        status = ""
        if obj.status == 'PAID':
            status="PAGO"
        return format_html(
            '<b style="color:{};">{}</b>',
            color,
            status
        )

    get_person_name.short_description = 'Nome'
    get_person_whatsapp.short_description = 'Whats'
    get_person_email.short_description = 'Email'


class PlanPricesAdmin(admin.ModelAdmin):
    list_display = ('vehicle_price_from','vehicle_price_to',
                    'plan_price')

class PlanPriceInline(admin.StackedInline):
    model = models.PlanPrice
    extra = 0


class VehicleSpecieAdmin(admin.ModelAdmin):

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):

        if db_field.name == 'vehicle_type':
            kwargs['widget'] = CheckboxSelectMultiple()
            kwargs['help_text'] = ''

        return db_field.formfield(**kwargs)


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
    elif model_name == "vehiclespecie":
        admin.site.register(model,VehicleSpecieAdmin)
    elif model_name == "chosenplan":
        admin.site.register(model,ChosenPlanAdmin)
    else:
        admin.site.register(model)