from django.urls import path, include
from rest_framework import routers
from email_service import views

app_name = 'email_service'

router = routers.DefaultRouter()
router.register('send', views.EmailServiceViewSet, basename="send")

urlpatterns = [
    path('', include(router.urls)),
]