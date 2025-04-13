from .common import WorkoutSerializer
# from users.serializers import UserSerializer
from routines.serializers.common import RoutineSerializer
from workout_exercises.serializers.common import WorkoutExerciseSerializer

class PopulatedWorkoutSerializer(WorkoutSerializer):
    # owner = 
    routine = RoutineSerializer()
    exercises = WorkoutExerciseSerializer(many=True)