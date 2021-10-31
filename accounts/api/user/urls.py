from django.urls import path, include

from accounts.api.user.views import UserDetailAPIView

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='user-detail'),
]
