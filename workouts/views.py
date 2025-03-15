from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import WorkoutSerializer

# Model
from .models import Workout

# Create your views here.

class ListCreateWorkoutView(APIView):

    # Index Controller
    # Route: GET /workouts/
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /workouts/
    def post(self, request):
        try:
            new_workout = WorkoutSerializer(data=request.data)
            if new_workout.is_valid():
                new_workout.save()
                return Response(new_workout.data, status.HTTP_201_CREATED)
            return Response(new_workout.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response('An unknown error occurred', status.HTTP_500_INTERNAL_SERVER_ERROR)