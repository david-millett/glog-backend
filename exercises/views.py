from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExerciseSerializer
from utils.exceptions import handle_exceptions

# Model
from .models import Exercise

# Create your views here.
class ListCreateExerciseView(APIView):

    # Index Controller
    # Route: GET /exercises/
    @handle_exceptions
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /exercises/
    @handle_exceptions
    def post(self, request):
        new_exercise = ExerciseSerializer(data=request.data)
        new_exercise.is_valid(raise_exception=True)
        new_exercise.save()
        return Response(new_exercise.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyExerciseView(APIView):

    # Show Controller
    # Route: GET /exercises/:pk/
    @handle_exceptions
    def get(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        seralizer = ExerciseSerializer(exercise)
        return Response(seralizer.data)
        
    # Delete Controller
    # Route: DELETE /exercises/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route: PUT /exercises/:pk/
    @handle_exceptions
    def put(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)