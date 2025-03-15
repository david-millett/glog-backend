from django.urls import path
from .views import ListCreateWorkoutView

urlpatterns = [
    path('', ListCreateWorkoutView.as_view())
]