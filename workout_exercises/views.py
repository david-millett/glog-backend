from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.common import WorkoutExerciseSerializer
from utils.exceptions import handle_exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.permissions import IsAdminOrReadOnly

# ! Check permission classes

# Model
from .models import WorkoutExercise

# Create your views here.
class ListCreateWorkoutExerciseView(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]

    # Index Controller
    # Route: GET /workout_exercises/
    @handle_exceptions
    def get(self, request):
        workout_exercises = WorkoutExercise.objects.all()
        serializer = WorkoutExerciseSerializer(workout_exercises, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /workout_exercises/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_workout_exercise = WorkoutExerciseSerializer(data=request.data)
        new_workout_exercise.is_valid(raise_exception=True)
        new_workout_exercise.save()
        return Response(new_workout_exercise.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyWorkoutExerciseView(APIView):
    permission_classes=[IsAdminOrReadOnly]

    # Show Controller
    # Route: GET /workout_exercises/:pk/
    @handle_exceptions
    def get(self, request, pk):
        workout_exercise = WorkoutExercise.objects.get(pk=pk)
        self.check_object_permissions(request, workout_exercise)
        seralizer = WorkoutExerciseSerializer(workout_exercise)
        return Response(seralizer.data)
        
    # Delete Controller
    # Route: DELETE /workout_exercises/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        workout_exercise = WorkoutExercise.objects.get(pk=pk)
        self.check_object_permissions(request, workout_exercise)
        workout_exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route: PUT /workout_exercises/:pk/
    @handle_exceptions
    def put(self, request, pk):
        workout_exercise = WorkoutExercise.objects.get(pk=pk)
        self.check_object_permissions(request, workout_exercise)
        serializer = WorkoutExerciseSerializer(workout_exercise, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
