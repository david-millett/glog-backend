from .common import WorkoutLogSerializer
from exercise_logs.serializers.common import ExerciseLogSerializer
from workouts.serializers.common import WorkoutSerializer
from routines.serializers.common import RoutineSerializer

class PopulatedWorkoutLogSerializer(WorkoutLogSerializer):
    exercises = ExerciseLogSerializer(many=True)
    workout = WorkoutSerializer()
    routine = RoutineSerializer()