from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model, hashers
from django.db.models import Q
from utils.exceptions import handle_exceptions

# Model
User = get_user_model()

# Create your views here.
class SignUpView(APIView):

    @handle_exceptions
    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        return Response('HIT SIGN UP ROUTE')
    
class SignInView(APIView):

    @handle_exceptions
    def post(self, request):
        u_or_e = request.data.get('username_or_email')
        password = request.data.get('password')
        user = User.objects.get(Q(username=u_or_e) | Q(email=u_or_e))
        if hashers.check_password(password, user.password):
            token_pair = RefreshToken.for_user(user)
            serialized_user = UserSerializer(user)
            return Response({
                'user': serialized_user.data,
                'token': str(token_pair.access_token)
            })
        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)