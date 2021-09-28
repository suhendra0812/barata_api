from rest_framework import generics
from .models import Beam, CosmoSkyMedPlan, RadarsatPlan, Satellite, Sensor
from .serializers import BeamSerializer, CosmoSkyMedPlanSerializer, RadarsatPlanSerializer, SatelliteSerializer, SensorSerializer

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


class CosmoSkyMedPlanAPIListView(generics.ListCreateAPIView):
    queryset = CosmoSkyMedPlan.objects.all()
    serializer_class = CosmoSkyMedPlanSerializer


class RadarsatPlanAPIListView(generics.ListCreateAPIView):
    queryset = RadarsatPlan.objects.all()
    serializer_class = RadarsatPlanSerializer