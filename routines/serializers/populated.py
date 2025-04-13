from .common import RoutineSerializer
# from users.serializers import UserSerializer
from workouts.serializers.common import WorkoutSerializer

class PopulatedRoutineSerializer(RoutineSerializer):
    # owner = UserSerializer()
    workouts = WorkoutSerializer(many=True)