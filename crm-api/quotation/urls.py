from django.urls import path, include
from rest_framework import routers
from quotation import views

app_name = 'quotation'

router = routers.DefaultRouter()
router.register('person', views.PersonViewSet, basename="person")
router.register('vehicle', views.VehicleViewSet, basename="vehicle")
router.register('plan', views.PlanViewSet, basename="plan")
router.register('chosen-plan', views.ChosenPlanViewSet, basename="chosen-plan")
router.register('vehicle-specie', views.VehicleSpecieViewSet, basename="vehicle-specie")
router.register('vehicle-type', views.VehicleTypeViewSet, basename="vehicle-type")

urlpatterns = [
    path('', include(router.urls)),
]