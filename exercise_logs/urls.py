from django.urls import path
from .views import ListCreateExerciseLogView, RetrieveUpdateDestroyExerciseLogView

urlpatterns = [
    path('', ListCreateExerciseLogView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyExerciseLogView.as_view())
]