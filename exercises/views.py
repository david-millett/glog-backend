from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ExerciseSerializer

# Model
from .models import Exercise

# Create your views here.
class ListCreateExerciseView(APIView):

    # Index Controller
    # Route: GET /exercises
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)