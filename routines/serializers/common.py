from rest_framework.serializers import ModelSerializer
from ..models import Routine

class RoutineSerializer(ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'
        # fields = ['id', 'workouts'] can add workouts in like this, but doesn't work with all