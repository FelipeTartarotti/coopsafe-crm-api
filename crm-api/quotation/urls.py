from django.urls import path, include
from rest_framework import routers
from quotation import views

app_name = 'quotation'

router = routers.DefaultRouter()
router.register('person', views.PersonViewSet, basename="person")
router.register('vehicle', views.VehicleViewSet, basename="vehicle")
router.register('plan', views.PlanViewSet, basename="plan")

urlpatterns = [
    path('', include(router.urls)),
]