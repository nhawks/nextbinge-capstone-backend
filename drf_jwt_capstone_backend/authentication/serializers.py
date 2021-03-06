from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "streaming_providers",
        )

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            streaming_providers=validated_data["streaming_providers"]
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
