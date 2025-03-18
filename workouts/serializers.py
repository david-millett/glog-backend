from rest_framework.serializers import ModelSerializer
from exercises.serializers import ExerciseSerializer
from .models import Workout

class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class PopulatedWorkoutSerializer(WorkoutSerializer):
    exercises = ExerciseSerializer(many=True)