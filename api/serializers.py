from rest_framework import serializers

from .models import RadarsatPlan, Satellite, Sensor, Beam, CosmoSkyMedPlan


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


class CosmoSkyMedPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmoSkyMedPlan
        fields = '__all__'


class RadarsatPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadarsatPlan
        fields = '__all__'