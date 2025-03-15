from django.urls import path
from .views import ListCreateExerciseView, RetrieveUpdateDestroyExerciseView

urlpatterns = [
    path('', ListCreateExerciseView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyExerciseView.as_view())
]