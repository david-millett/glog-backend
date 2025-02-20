from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    rep_min = models.PositiveIntegerField()
    rep_max = models.PositiveIntegerField(blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    # category = 
    # owner = 

    def __str__(self):
        return f'{self.name}'