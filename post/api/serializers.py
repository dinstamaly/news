from rest_framework import serializers
from rest_framework.reverse import reverse

from accounts.api.serializers import UserPublicSerializer
from post.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = UserPublicSerializer(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    upvote_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'user',
            'title',
            'link',
            'upvote_url',
            'upvotes',
            'creation_date',
            'comments'
        ]
        read_only_fields = ['user']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

    def get_upvote_url(self, obj):
        request = self.context.get('request')
        return reverse("upvote", kwargs={'id': obj.id}, request=request)
