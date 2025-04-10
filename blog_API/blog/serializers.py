from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import BlogPost
from blog.models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]
                  
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = 'Post'
        fields = ['id', 'title', 'body', 'owner']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']       


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = 'Post'
        fields = ['id', 'title', 'body', 'owner', 'comments']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']
