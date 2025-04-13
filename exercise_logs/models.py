from django.db import models

# Create your models here.
class ExerciseLog(models.Model):
    owner = models.ForeignKey(
        to='users.User',
        related_name='exercises_logged',
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        to='exercises.Exercise',
        related_name='logs',
        on_delete=models.CASCADE
    )
    workout_log = models.ForeignKey(
        to='workout_logs.WorkoutLog',
        related_name='exercises',
        on_delete=models.CASCADE
    )
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight_kg = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return {self.date}
