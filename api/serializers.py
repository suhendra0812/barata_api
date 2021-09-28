from rest_framework import serializers

from .models import Satellite, Sensor, Beam, Planning


class SatelliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satellite
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class BeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beam
        fields = '__all__'


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = '__all__'