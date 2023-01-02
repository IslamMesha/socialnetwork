from rest_framework import serializers

from social.models import Like, Post


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "likes",
            "content",
        ]
        extra_kwargs = {"user": {"read_only": True}}

    @staticmethod
    def get_likes(obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = ["user", "post"]
