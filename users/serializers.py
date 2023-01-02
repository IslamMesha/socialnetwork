from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from users.models import User
from users.utils import get_user_ip
from users.validators import validate_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validate_email],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password", "placeholder": "Password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )
        user.set_password(validated_data["password"])
        user.ipaddress = get_user_ip(self.context["request"])
        user.save()
        return user
