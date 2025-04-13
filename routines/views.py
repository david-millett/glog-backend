from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.common import RoutineSerializer
from .serializers.populated import PopulatedRoutineSerializer
from utils.exceptions import handle_exceptions
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwner

# Model
from .models import Routine

# Create your views here.
class ListCreateRoutineView(APIView):
    permission_classes=[IsAuthenticated]

    # Index Controller
    # Route: GET /routines/
    @handle_exceptions
    def get(self, request):
        routines = Routine.objects.all()
        serializer = PopulatedRoutineSerializer(routines, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /routines/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_routine = RoutineSerializer(data=request.data)
        new_routine.is_valid(raise_exception=True)
        new_routine.save()
        return Response(new_routine.data, status.HTTP_201_CREATED)
        
class RetrieveUpdateDestroyRoutineView(APIView):
    permission_classes=[IsOwner]

    # Show Controller
    # Route: GET /routines/:pk/
    @handle_exceptions
    def get(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        self.check_object_permissions(request, routine)
        seralizer = PopulatedRoutineSerializer(routine)
        return Response(seralizer.data)
        
    # Delete Controller
    # Route: DELETE /routines/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        self.check_object_permissions(request, routine)
        routine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route: PUT /routines/:pk/
    @handle_exceptions
    def put(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        self.check_object_permissions(request, routine)
        serializer = RoutineSerializer(routine, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)