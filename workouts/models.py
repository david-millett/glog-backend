from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    # Type? So instead of workouts could add activities like running, swimming, yoga

    def __str__(self):
        return f'{self.name} (Created {self.created})'