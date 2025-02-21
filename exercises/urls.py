from django.urls import path
from .views import ListCreateExerciseView

urlpatterns = [
    path('', ListCreateExerciseView.as_view())
]