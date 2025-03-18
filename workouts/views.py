from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WorkoutSerializer, PopulatedWorkoutSerializer
from utils.exceptions import handle_exceptions
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner

# Model
from .models import Workout

# Create your views here.
class ListCreateWorkoutView(APIView):
    permission_classes=[IsAuthenticated]

    # Index Controller
    # Route: GET /workouts/
    @handle_exceptions
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = PopulatedWorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /workouts/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_workout = WorkoutSerializer(data=request.data)
        new_workout.is_valid(raise_exception=True)
        new_workout.save()
        return Response(new_workout.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyWorkoutView(APIView):
    permission_classes=[IsOwner]
        
    # Show Controller
    # Route: GET /workouts/:pk/
    @handle_exceptions
    def get(self, request, pk):
        workout = Workout.objects.get(pk=pk)
        self.check_object_permissions(request, workout)
        serializer = PopulatedWorkoutSerializer(workout)
        return Response(serializer.data)

    # Delete Controller
    # Route: DELETE /workouts/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        workout = Workout.objects.get(pk=pk)
        self.check_object_permissions(request, workout)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route PUT /workouts/:pk/
    @handle_exceptions
    def put(self, request, pk):
        workout = Workout.objects.get(pk=pk)
        self.check_object_permissions(request, workout)
        serializer = WorkoutSerializer(workout, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)