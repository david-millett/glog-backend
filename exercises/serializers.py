from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .models import Exercise

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class PopulatedExerciseSerializer(ExerciseSerializer):
    owner = UserSerializer()
