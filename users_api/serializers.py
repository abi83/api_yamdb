from users_api.models import YamdbUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RoleField(serializers.ChoiceField):

    # def to_representation(self, value):
    #     return str(value)[2:].split("'")[0]

    def to_internal_value(self, data):
        if not data:
            return YamdbUser.USER

        if data not in ['user', 'admin', 'moderator']:
            raise serializers.DjangoValidationError(
                "Field 'role' must be in ['user', 'admin', 'moderator']")

        if data == 'user':
            return YamdbUser.USER
        elif data == 'moderator':
            return YamdbUser.MODERATOR
        elif data == 'admin':
            return YamdbUser.ADMIN

        raise serializers.ValidationError('Something went extremely wrong')




class MeSerializer(serializers.ModelSerializer):
    # url = serializers.ReadOnlyField(source='username', read_only=True)
    username = serializers.ReadOnlyField()
    # role = RoleField(choices=YamdbUser.CHOICES, default=YamdbUser.USER)
    # role = serializers.CharField(source='get_role_display')
    role = serializers.CharField(source='_role', required=False)


    # def to_internal_value(self, data):
    #     breakpoint()
    #     data['_role'] = data['role'] or None
    #     return data


    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'role',
                  # 'url',
                  ]
        lookup_field = 'username'
        # extra_kwargs = {'url': {'lookup_field': 'username'}}




class UserSerializer(serializers.ModelSerializer):

    # role = RoleField(choices=YamdbUser.CHOICES, default=YamdbUser.USER)
    role = serializers.CharField(source='_role', required=False)

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

    # def to_internal_value(self, data):
    #     breakpoint()
    #     data['_role'] = data.get('role', None)
    #     return {k:v for k,v in data.items() if k !='role'}

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'role',
                  ]
        lookup_field = 'username'


