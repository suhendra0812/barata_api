from rest_framework import generics
from .models import Beam, Planning, Satellite, Sensor
from .serializers import BeamSerializer, PlanningSerializer, SatelliteSerializer, SensorSerializer

# Create your views here.


class SatelliteAPIListView(generics.ListCreateAPIView):
    queryset = Satellite.objects.all()
    serializer_class = SatelliteSerializer


class SensorAPIListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class BeamAPIListView(generics.ListCreateAPIView):
    queryset = Beam.objects.all()
    serializer_class = BeamSerializer


class PlanningAPIListView(generics.ListCreateAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer