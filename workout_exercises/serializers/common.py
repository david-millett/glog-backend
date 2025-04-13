from rest_framework.serializers import ModelSerializer
from ..models import WorkoutExercise

class WorkoutExerciseSerializer(ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'
