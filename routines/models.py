from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)