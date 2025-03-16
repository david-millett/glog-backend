from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from utils.exceptions import handle_exceptions

# Model
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(APIView):

    @handle_exceptions
    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        return Response('HIT SIGN UP ROUTE')