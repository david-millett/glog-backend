from rest_framework.serializers import ModelSerializer
from workouts.serializers import WorkoutSerializer
from .models import Routine

class RoutineSerializer(ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'

class PopulatedRoutineSerializer(RoutineSerializer):
    workouts = WorkoutSerializer(many=True)