from django.urls import path, include
from rest_framework import routers
from payment import views

app_name = 'payment'

router = routers.DefaultRouter()
router.register('credit-card', views.CreditCardViewSet, basename="credit-card")

urlpatterns = [
    path('', include(router.urls)),
]