from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    rep_min = models.PositiveIntegerField()
    rep_max = models.PositiveIntegerField(blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(
        to='users.User',
        related_name='created_exercises',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'