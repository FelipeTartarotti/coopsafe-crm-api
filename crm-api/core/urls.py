from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include(([
        path('email/', include('email_service.urls')),
        path('fipe/', include('fipe.urls')),
        path('quotation/', include('quotation.urls')),
    ], 'api'))),
]