from django.db import models

# Create your models here.


class Relat(models.Model):
    title = models.CharField(max_length=100, default='')
