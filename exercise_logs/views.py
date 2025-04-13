from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.common import ExerciseLogSerializer
from .serializers.populated import PopulatedExerciseLogSerializer
from utils.exceptions import handle_exceptions
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner

# Model
from .models import ExerciseLog

# Create your views here.
class ListCreateExerciseLogView(APIView):
    permission_classes=[IsAuthenticated]

    # Index Controller
    # Route: GET /exercise_logs/
    @handle_exceptions
    def get(self, request):
        exercise_logs = ExerciseLog.objects.all()
        serializer = PopulatedExerciseLogSerializer(exercise_logs, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /exercise_logs/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_exercise_log = ExerciseLogSerializer(data=request.data)
        new_exercise_log.is_valid(raise_exception=True)
        new_exercise_log.save()
        return Response(new_exercise_log.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyExerciseLogView(APIView):
    permission_classes=[IsOwner]
        
    # Show Controller
    # Route: GET /exercise_logs/:pk/
    @handle_exceptions
    def get(self, request, pk):
        exercise_log = ExerciseLog.objects.get(pk=pk)
        self.check_object_permissions(request, exercise_log)
        serializer = PopulatedExerciseLogSerializer(exercise_log)
        return Response(serializer.data)

    # Delete Controller
    # Route: DELETE /exercise_logs/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        exercise_log = ExerciseLog.objects.get(pk=pk)
        self.check_object_permissions(request, exercise_log)
        exercise_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route PUT /exercise_logs/:pk/
    @handle_exceptions
    def put(self, request, pk):
        exercise_log = ExerciseLog.objects.get(pk=pk)
        self.check_object_permissions(request, exercise_log)
        serializer = ExerciseLogSerializer(exercise_log, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)