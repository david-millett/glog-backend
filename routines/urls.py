from django.urls import path
from .views import ListCreateRoutineView, RetrieveUpdateDestroyRoutineView

urlpatterns = [
    path('', ListCreateRoutineView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyRoutineView.as_view())
]