from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView, DestroyAPIView
)
from django.shortcuts import get_object_or_404
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin, DestroyModelMixin,
)
from django.views.generic import RedirectView
from accounts.api.permissions import IsOwnerOrReadOnly
from post.api.serializers import PostSerializer
from post.models import Post


class PostListAPIView(CreateModelMixin, ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostUpdateAPIView(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDeleteAPIView(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class UpvoteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Post, id=self.kwargs['id'])
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.upvotes.all():
                obj.upvotes.remove(user)
            else:
                obj.upvotes.add(user)

        return url_



