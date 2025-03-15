from rest_framework.serializers import ModelSerializer
from .models import Routine

class RoutineSerializer(ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'