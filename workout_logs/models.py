from django.db import models

# Create your models here.
class WorkoutLog(models.Model):
    owner = models.ForeignKey(
        to='users.User',
        related_name='workouts_logged',
        on_delete=models.CASCADE
    )
    workout = models.ForeignKey(
        to='workouts.Workout',
        related_name='logs',
        on_delete=models.CASCADE
    )
    routine = models.ForeignKey(
        to='routines.Routine',
        related_name='workouts_logged',
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return {self.date}