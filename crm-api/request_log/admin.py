from django.contrib import admin
from django.apps import	apps
from request_log import models

class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('endpoint','status_code',
                    'method','ip','user',
                    'time', 'response_time')

admin.site.register(models.RequestLog,RequestLogAdmin)

