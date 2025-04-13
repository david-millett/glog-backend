from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        to='users.User',
        related_name='created_workouts',
        on_delete=models.CASCADE
    )
    routine = models.ForeignKey(
        to='routines.Routine',
        related_name='workouts',
        on_delete=models.CASCADE
    )
    day = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} (Created {self.created})'