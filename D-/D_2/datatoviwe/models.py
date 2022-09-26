from django.db import models

# Create your models here.


class Store(models.Model):
    proid  = models.IntegerField()
    proname = models.CharField(max_length=70)
    prodisc = models.CharField(max_length=200)
    protype = models.CharField(max_length=70)

    def __str__(self):
        return self.proname

