from rest_framework.serializers import ModelSerializer
# from routines.serializers import RoutineSerializer
# from workout_exercises.serializers import WorkoutExerciseSerializer
from ..models import Workout

class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

# class PopulatedWorkoutSerializer(WorkoutSerializer):
#     # owner = 
#     routine = RoutineSerializer()
#     exercises = WorkoutExerciseSerializer(many=True)