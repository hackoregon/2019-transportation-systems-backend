# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import GeometryField


class NcdbSampleTransportationCommute(models.Model):
    tract_geo_fips = models.TextField(primary_key=True)
    t128_001_17 = models.IntegerField(blank=True, null=True)
    t128_002_17 = models.IntegerField(blank=True, null=True)
    t128_009_17 = models.IntegerField(blank=True, null=True)
    t128_010_17 = models.IntegerField(blank=True, null=True)
    t128_003_17 = models.IntegerField(blank=True, null=True)
    t128_004_17 = models.IntegerField(blank=True, null=True)
    t128_005_17 = models.IntegerField(blank=True, null=True)
    t128_006_17 = models.IntegerField(blank=True, null=True)
    t128_007_17 = models.IntegerField(blank=True, null=True)
    t128_008_17 = models.IntegerField(blank=True, null=True)
    t129_001_17 = models.IntegerField(blank=True, null=True)
    t129_002_17 = models.IntegerField(blank=True, null=True)
    t129_003_17 = models.IntegerField(blank=True, null=True)
    t129_004_17 = models.IntegerField(blank=True, null=True)
    t129_005_17 = models.IntegerField(blank=True, null=True)
    t129_006_17 = models.IntegerField(blank=True, null=True)
    t129_007_17 = models.IntegerField(blank=True, null=True)
    t129_008_17 = models.IntegerField(blank=True, null=True)
    t129_009_17 = models.IntegerField(blank=True, null=True)
    t129_010_17 = models.IntegerField(blank=True, null=True)
    t147_001_17 = models.IntegerField(blank=True, null=True)
    opp_zone = models.BooleanField(blank=True, null=True)
    opp_zone_elig = models.TextField(blank=True, null=True)
    geom_multpoly_4326 = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncdb_sample_transportation_commute'
