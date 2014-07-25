from django.db import models
from django.contrib.gis.db import models as gis_models


class FoodTruck(models.Model):
	applicant = models.TextField()
	loc_desc = models.TextField()
	fooditems = models.TextField(null=True)
	schedule = models.TextField()
	latitude = models.FloatField()
 	longitude = models.FloatField()
 	geom = gis_models.GeometryField(srid=4326, null=True)
