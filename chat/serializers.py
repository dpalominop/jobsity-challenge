from .models import Room, Post
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.Serializer):
    message = serializers.CharField()
    author = serializers.CharField()
    created_date = serializers.CharField()
    created_time = serializers.CharField()
