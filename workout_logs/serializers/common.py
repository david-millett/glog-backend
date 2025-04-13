from rest_framework.serializers import ModelSerializer
from ..models import WorkoutLog

class WorkoutLogSerializer(ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = '__all__'