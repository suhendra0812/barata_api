from django.db import models

# Create your models here.
import os
import glob
import pandas as pd


SATELLITES = [
    ('COSMO-SkyMed 1', 'COSMO-SkyMed 1'),
    ('COSMO-SkyMed 2', 'COSMO-SkyMed 2'),
    ('COSMO-SkyMed 3', 'COSMO-SkyMed 3'),
    ('COSMO-SkyMed 4', 'COSMO-SkyMed 4'),
    ('RADARSAT-2', 'RADARSAT-2'),
]

SENSORS = [
    ('StripMap (HIMAGE)', 'StripMap (HIMAGE)'),
    ('ScanSAR (WideRegion)', 'ScanSAR (WideRegion)'),
    ('ScanSAR (HugeRegion)', 'ScanSAR (HugeRegion)'),
    ('High Incidence', 'High Incidence'),
    ('Extra Fine', 'Extra Fine'),
    ('ScanSAR Narrow', 'ScanSAR Narrow'),
]

BEAMS = [
    ('H4-0A','H4-0A'), ('H4-0B','H4-0B'), ('H4-01','H4-01'), ('H4-02','H4-02'), ('H4-03','H4-03'), ('H4-04', 'H4-04'), ('H4-05','H4-05'), ('H4-06','H4-06'), ('H4-07','H4-07'), ('H4-08','H4-08'), ('H4-09','H4-09'), ('H4-10','H4-10'), ('H4-11','H4-11'), ('H4-12','H4-12'), ('H4-13','H4-13'), ('H4-14','H4-14'), ('H4-15','H4-15'), ('H4-16','H4-16'), ('H4-17','H4-17'), ('H4-18','H4-18'), ('H4-19','H4-19'), ('H4-20','H4-20'), ('H4-21','H4-21'), ('H4-22','H4-22'), ('H4-23','H4-23'), ('H4-24','H4-24'),
    ('WR-00','WR-00'), ('WR-01','WR-01'), ('WR-02','WR-02'), ('WR-03','WR-03'), ('WR-04','WR-04'), ('WR-05','WR-05'), ('WR-06','WR-06'), ('WR-07','WR-07'),
    ('HG-00','HG-00'), ('HG-01','HG-01'), ('HG-02','HG-02'), ('HG-03','HG-03'), ('HG-04','HG-04'), ('HG-05','HG-05'),
    ('EH1','EH1'), ('EH2','EH2'), ('EH3','EH3'), ('EH4','EH4'), ('EH5','EH5'), ('EH6','EH6'),
    ('XF0W1','XF0W1'), ('XF0W2','XF0W2'), ('XF0W3','XF0W3'), ('XF0S7','XF0S7'),
    ('SCNA','SCNA'), ('SCNB','SCNB'),
]

POLARISATIONS = [
    ('HH', 'HH'),
    ('VV', 'VV')
]

SIDES = [
    ('Right', 'Right'),
    ('Left', 'Left'),
]

def get_angle(beam):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    beam_paths = glob.glob(os.path.join(base_dir, 'beam/*/*.csv'))
    beam_df = pd.concat([pd.read_csv(beam_path) for beam_path in beam_paths], ignore_index=True)
    near_angle = beam_df.loc[beam_df['BEAM'] == beam, 'NEAR'].values
    far_angle = beam_df.loc[beam_df['BEAM'] == beam, 'FAR'].values
    angle = (near_angle + far_angle) / 2
    
    return angle


class Satellite(models.Model):
    name = models.CharField(max_length=20, choices=SATELLITES)

    class Meta:
        db_table = "satellite"
    
    def __str__(self):
        return self.name
    

class Sensor(models.Model):
    satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, choices=SENSORS)

    class Meta:
        db_table = "sensor"
    
    def __str__(self):
        return self.name


class Beam(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=BEAMS)

    class Meta:
        db_table = "beam"

    def __str__(self):
        return self.name


class CosmoSkyMedPlan(models.Model):
    order_id = models.IntegerField(unique=True)
    pr_id = models.IntegerField(unique=True)
    satellite = models.ForeignKey(Satellite, on_delete=models.SET_NULL, null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True, blank=True)
    beam = models.ForeignKey(Beam, on_delete=models.SET_NULL, null=True, blank=True)
    polarisation = models.CharField(max_length=2, choices=POLARISATIONS)
    side = models.CharField(max_length=5, choices=SIDES)
    angle = models.FloatField(null=True, blank=True)
    sensing_start = models.DateTimeField()
    sensing_stop = models.DateTimeField()
    visibility_start = models.DateTimeField(null=True, blank=True)
    visibility_stop = models.DateTimeField(null=True, blank=True)
    scene_number = models.IntegerField()
    user = models.CharField(max_length=50, null=True, blank=True)
    application = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "csk_plan"
        verbose_name = "COSMO-SkyMed Plan"

    def __str__(self):
        return str(self.order_id)


class RadarsatPlan(models.Model):
    order_id = models.IntegerField(unique=True)
    satellite = models.ForeignKey(Satellite, on_delete=models.SET_NULL, null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True, blank=True)
    beam = models.ForeignKey(Beam, on_delete=models.SET_NULL, null=True, blank=True)
    polarisation = models.CharField(max_length=2, choices=POLARISATIONS)
    side = models.CharField(max_length=5, choices=SIDES)
    angle = models.FloatField(null=True, blank=True)
    sensing_start = models.DateTimeField()
    sensing_stop = models.DateTimeField()
    downlink_start = models.DateTimeField(null=True, blank=True)
    downlink_stop = models.DateTimeField(null=True, blank=True)
    scene_number = models.IntegerField()
    user = models.CharField(max_length=50, null=True, blank=True)
    application = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "rs_plan"
        verbose_name = "RADARSAT-2 Plan"

    def __str__(self):
        return str(self.order_id)
    
    