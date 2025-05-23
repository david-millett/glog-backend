# Generated by Django 4.2.20 on 2025-04-13 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0003_remove_exercise_owner_remove_exercise_rep_max_and_more'),
        ('workout_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField()),
                ('reps', models.PositiveIntegerField()),
                ('weight_kg', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='exercises.exercise')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_logged', to=settings.AUTH_USER_MODEL)),
                ('workout_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workout_logs.workoutlog')),
            ],
        ),
    ]
