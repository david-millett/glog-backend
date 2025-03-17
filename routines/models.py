from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        to='users.User',
        related_name='created_routines',
        on_delete=models.CASCADE
    )
    workouts = models.ManyToManyField(
        to='workouts.Workout',
        related_name='routines',
        blank=True
    )

    def __str__(self):
        return f'{self.name} (Created {self.created})'