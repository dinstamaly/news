from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from accounts.api.user.serializers import UserDetailSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = "username"