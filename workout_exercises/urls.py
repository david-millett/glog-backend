from django.urls import path
from .views import ListCreateWorkoutExerciseView, RetrieveUpdateDestroyWorkoutExerciseView

urlpatterns = [
    path('', ListCreateWorkoutExerciseView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyWorkoutExerciseView.as_view())
]