from django.db import models

class MyModel(models.Model):
    x_field = models.CharField(max_length=100)
    y_field = models.IntegerField()
