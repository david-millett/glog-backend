from django.urls import path
from .views import ListCreateWorkoutView, RetrieveUpdateDestroyWorkoutView

urlpatterns = [
    path('', ListCreateWorkoutView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyWorkoutView.as_view())
]