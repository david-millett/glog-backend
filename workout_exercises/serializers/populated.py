from .common import WorkoutExerciseSerializer
from exercises.serializers import ExerciseSerializer
from workouts.serializers.common import WorkoutSerializer

class PopulatedWorkoutExerciseSerializer(WorkoutExerciseSerializer):
    exercise = ExerciseSerializer()
    workout = WorkoutSerializer()