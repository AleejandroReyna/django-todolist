from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from auth import serializers


class CreateUserView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )


class LoginView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer
