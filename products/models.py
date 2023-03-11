from django.db import models


class Version(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    software = models.CharField(max_length=25)
    version = models.CharField(max_length=25)

