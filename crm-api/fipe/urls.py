from django.urls import path, include
from rest_framework import routers
from fipe import views

app_name = 'fipe'

router = routers.DefaultRouter()
router.register('consult', views.FipeViewSet, basename="consult")

urlpatterns = [
    path('', include(router.urls)),
]