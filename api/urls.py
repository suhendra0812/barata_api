from django.urls import path
from .views import BeamAPIListView, CosmoSkyMedPlanAPIListView, RadarsatPlanAPIListView, SatelliteAPIListView, SensorAPIListView


urlpatterns = [
    path('satellite/', SatelliteAPIListView.as_view(), name='satellite_api'),
    path('sensor/', SensorAPIListView.as_view(), name='sensor_api'),
    path('beam/', BeamAPIListView.as_view(), name='beam_api'),
    path('csk-plan/', CosmoSkyMedPlanAPIListView.as_view(), name='cskplan_api'),
    path('rs-plan/', RadarsatPlanAPIListView.as_view(), name='rsplan_api'),
]
