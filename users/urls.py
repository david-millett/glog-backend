from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignUpView, SignInView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/', SignInView.as_view())
]