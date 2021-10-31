from django.urls import path

from post.api.comments.views import CommentList, CommentDetail
from post.api.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    UpvoteView,
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:id>/upvote/', UpvoteView.as_view(), name="upvote"),
    path('<int:id>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', PostDeleteAPIView.as_view(), name='delete'),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]