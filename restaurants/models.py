from django.db import models
from django.contrib.localflavor.us.models import USStateField


class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = USStateField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.name
