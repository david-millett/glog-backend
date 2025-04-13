from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        to='users.User',
        related_name='created_routines',
        on_delete=models.CASCADE
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} (Created {self.created})'