from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import PasswordField

from users_api.models import YamdbUser


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей"""
    role = serializers.CharField(required=False)

    username = serializers.CharField(
        max_length=64,
        min_length=5,
        allow_blank=False,
        trim_whitespace=True,
        validators=[UniqueValidator(queryset=YamdbUser.objects.all())]
    )
    email = serializers.EmailField(
        min_length=5,
        validators=[UniqueValidator(queryset=YamdbUser.objects.all())]
    )

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'bio', 'role', ]
        lookup_field = 'username'


class EmailRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для преобразования данных при получении кода подтверждения.
    """
    password = PasswordField(required=False)
    username_field = 'email'

    class Meta:
        model = YamdbUser
        fields = ['email', 'password', ]


class UserVerificationSerializer(serializers.ModelSerializer):
    password = PasswordField(required=False)
    confirmation_code = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(required=False)
    username_field = 'email'

    class Meta:
        model = YamdbUser
        fields = ['email', 'password', 'confirmation_code', 'is_active']
