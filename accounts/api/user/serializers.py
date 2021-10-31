from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse


class UserDetailSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'posts', 'comments']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse(
            "user-detail",
            kwargs={'username': obj.username},
            request=request)
