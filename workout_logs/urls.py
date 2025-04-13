from django.urls import path
from .views import ListCreateWorkoutLogView, RetrieveUpdateDestroyWorkoutLogView

urlpatterns = [
    path('', ListCreateWorkoutLogView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyWorkoutLogView.as_view())
]