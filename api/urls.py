from django.urls import path
from .views import BeamAPIListView, PlanningAPIListView, SatelliteAPIListView, SensorAPIListView


urlpatterns = [
    path('satellite/', SatelliteAPIListView.as_view(), name='satellite_api'),
    path('sensor/', SensorAPIListView.as_view(), name='sensor_api'),
    path('beam/', BeamAPIListView.as_view(), name='beam_api'),
    path('planning/', PlanningAPIListView.as_view(), name='plan_api'),
]
