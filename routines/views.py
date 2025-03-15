from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import RoutineSerializer

# Model
from .models import Routine

# Create your views here.
class ListCreateRoutineView(APIView):

    # Index Controller
    # Route: GET /routines/
    def get(self, request):
        routines = Routine.objects.all()
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)
    
    # Create Controller
    # Route: POST /routines/
    def post(self, request):
        try:
            new_routine = RoutineSerializer(data=request.data)
            if new_routine.is_valid():
                new_routine.save()
                return Response(new_routine.data, status.HTTP_201_CREATED)
            return Response(new_routine.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response ('An unknown error occurred', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RetrieveUpdateDestroyRoutineView(APIView):

    def get_routine(self, pk):
        try:
            return Routine.objects.get(pk=pk)
        except Routine.DoesNotExist as e:
            print('Error type ->', e.__class__.__name__)
            print(e)
            raise NotFound({ 'message': 'Routine not found' })

    # Show Controller
    # Route: GET /routines/:pk/
    def get(self, request, pk):
        routine = self.get_routine(pk)
        try:
            seralizer = RoutineSerializer(routine)
            return Response(seralizer.data)
        except Exception as e:
            print(e)
            return Response ({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Delete Controller
    # Route: DELETE /routines/:pk/
    def delete(self, request, pk):
        routine = self.get_routine(pk)
        try:
            routine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Update Controller
    # Route: PUT /routines/:pk/
    def put(self, request, pk):
        routine = self.get_routine(pk)
        try:
            serializer = RoutineSerializer(routine, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            print(e)
            return Response({ 'message': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)