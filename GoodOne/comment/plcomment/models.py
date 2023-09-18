from django.db import models

class Profile(models.Model):
    firstName = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    username = models.EmailField(max_length=30)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phoneNo = models.PositiveIntegerField()
