from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'group', 'image')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.SlugRelatedField(
        read_only=True, slug_field="id"
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('id', 'author', 'post', 'created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = ('following', 'user')
        model = Follow

    def create(self, validated_data):
        if self.is_valid():
            if validated_data["following"] == validated_data["user"]:
                raise serializers.ValidationError(
                    "Нельзя подписаться на самого себя!"
                )
            if Follow.objects.filter(**validated_data).exists():
                raise serializers.ValidationError(
                    "Вы уже подписаны на автора..."
                )
        return Follow.objects.create(**validated_data)
