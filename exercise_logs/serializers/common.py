from rest_framework.serializers import ModelSerializer
from ..models import ExerciseLog

class ExerciseLogSerializer(ModelSerializer):
    class Meta:
        model = ExerciseLog
        fields = '__all__'