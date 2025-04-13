from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.common import WorkoutLogSerializer
from .serializers.populated import PopulatedWorkoutLogSerializer
from utils.exceptions import handle_exceptions
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner

# Model
from .models import WorkoutLog

# Create your views here.
class ListCreateWorkoutLogView(APIView):
    permission_classes=[IsAuthenticated]

    # Index Controller
    # Route: GET /workout_logs/
    @handle_exceptions
    def get(self, request):
        workout_logs = WorkoutLog.objects.all()
        serializer = PopulatedWorkoutLogSerializer(workout_logs, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /workout_logs/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_workout_log = WorkoutLogSerializer(data=request.data)
        new_workout_log.is_valid(raise_exception=True)
        new_workout_log.save()
        return Response(new_workout_log.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyWorkoutLogView(APIView):
    permission_classes=[IsOwner]
        
    # Show Controller
    # Route: GET /workout_logs/:pk/
    @handle_exceptions
    def get(self, request, pk):
        workout_log = WorkoutLog.objects.get(pk=pk)
        self.check_object_permissions(request, workout_log)
        serializer = PopulatedWorkoutLogSerializer(workout_log)
        return Response(serializer.data)

    # Delete Controller
    # Route: DELETE /workout_logs/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        workout_log = WorkoutLog.objects.get(pk=pk)
        self.check_object_permissions(request, workout_log)
        workout_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route PUT /workout_logs/:pk/
    @handle_exceptions
    def put(self, request, pk):
        workout_log = WorkoutLog.objects.get(pk=pk)
        self.check_object_permissions(request, workout_log)
        serializer = WorkoutLogSerializer(workout_log, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)