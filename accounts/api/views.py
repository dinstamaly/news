from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer
