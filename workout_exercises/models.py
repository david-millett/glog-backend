from django.db import models

# Create your models here.
class WorkoutExercise(models.Model):
    owner = models.ForeignKey(
        to='users.User',
        related_name='workout_exercises',
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        to='exercises.Exercise',
        related_name='user_stats',
        on_delete=models.CASCADE
    )
    workout = models.ForeignKey(
        to='workouts.Workout',
        related_name='exercises',
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    rep_min = models.PositiveIntegerField()
    rep_max = models.PositiveIntegerField()
    weight_kg = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'User exercise {self.id}'