from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
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

    def get_exercise(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist as e:
            print('Error type ->', e.__class__.__name__)
            print(e)
            raise NotFound({ 'message': 'Exercise not found' })

    # Show Controller
    # Route: GET /exercises/:pk/
    def get(self, request, pk):
        exercise = self.get_exercise(pk)
        try:
            seralizer = ExerciseSerializer(exercise)
            return Response(seralizer.data)
        except Exception as e:
            print(e)
            return Response ({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Delete Controller
    # Route: DELETE /exercises/:pk/
    def delete(self, request, pk):
        exercise = self.get_exercise(pk)
        try:
            exercise.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Update Controller
    # Route: PUT /exercises/:pk/
    def put(self, request, pk):
        exercise = self.get_exercise(pk)
        try:
            serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)