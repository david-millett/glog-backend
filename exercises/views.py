from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExerciseSerializer

# Model
from .models import Exercise

# Create your views here.
class ListCreateExerciseView(APIView):

    # Index Controller
    # Route: GET /exercises/
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /exercises/
    def post(self, request):
        try:
            new_exercise = ExerciseSerializer(data=request.data)
            if new_exercise.is_valid():
                new_exercise.save()
                return Response(new_exercise.data, status.HTTP_201_CREATED)
            return Response(new_exercise.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response ('An unknown error occurred', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RetrieveUpdateDestroyExerciseView(APIView):

    # Show Controller
    # Route: GET /exercises/:pk/
    def get(self, request, pk):
        try:
            exercise = Exercise.objects.get(pk=pk)
            return Response('HIT SHOW ROUTE')
        except Exercise.DoesNotExist as e:
            print('Error type ->', e.__class__.__name__)
            print(e)
            return Response ({ 'message': 'Exercise does not exist' }, status.HTTP_404_NOT_FOUND)