from rest_framework import serializers
from rest_framework.reverse import reverse

from post.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'post']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)
