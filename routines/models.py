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