from .common import ExerciseLogSerializer
from exercises.serializers import ExerciseSerializer
from workout_logs.serializers.common import WorkoutLogSerializer

class PopulatedExerciseLogSerializer(ExerciseLogSerializer):
    workout_log = WorkoutLogSerializer()
    exercise = ExerciseSerializer()