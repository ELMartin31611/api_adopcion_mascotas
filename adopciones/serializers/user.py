from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    password = serializers.CharField(
        min_length=8,
        write_only=True
    )

    password2 = serializers.CharField(
        write_only=True
    )

    def validate_username(self, value):

        if User.objects.filter(
            username=value
        ).exists():

            raise serializers.ValidationError(
                "Este usuario ya existe."
            )

        return value

    def validate_email(self, value):

        if User.objects.filter(
            email=value
        ).exists():

            raise serializers.ValidationError(
                "Este correo ya existe."
            )

        return value

    def validate(self, data):

        if data["password"] != data["password2"]:

            raise serializers.ValidationError(
                {
                    "password2": "Las contraseñas no coinciden."
                }
            )

        return data

    def create(self, validated_data):

        validated_data.pop("password2")

        return User.objects.create_user(
            **validated_data
        )