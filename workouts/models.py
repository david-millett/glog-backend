from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(
        max_length=25,
        blank=True
    )
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        to='users.User',
        related_name='created_workouts',
        on_delete=models.CASCADE
    )
    exercises = models.ManyToManyField(
        to='exercises.Exercise',
        related_name='workouts',
        blank=True
    )
    # activities, so could add activities like running, swimming, yoga - create new app for this

    def __str__(self):
        return f'{self.name} (Created {self.created})'