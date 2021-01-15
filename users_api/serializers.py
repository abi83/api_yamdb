from users_api.models import YamdbUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class MeSerializer(serializers.ModelSerializer):
    # url = serializers.ReadOnlyField(source='username', read_only=True)
    username = serializers.ReadOnlyField()

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'role',
                  # 'url',
                  ]
        lookup_field = 'username'
        # extra_kwargs = {'url': {'lookup_field': 'username'}}

class RoleField(serializers.ChoiceField):

    def to_representation(self, value):
        # breakpoint()
        return str(value)[9:].split("'")[0]
        # return super(RoleField, self).to_representation()

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



class UserSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['role'] = str(ret['role'])[9:].split("'")[0]
    #     return ret
    #
    # def to_internal_value(self, data):
    #     if data.is_valid():
    #     ret = super().to_representation(data)
    #     role = ret.get('role')
    #     if not role or role not in ['user', 'admin', 'moderator']:
    #         raise serializers.DjangoValidationError(
    #             "Field 'role' must be in ['user', 'admin', 'moderator']")
    #
    #     if role == 'user':
    #         ret['role'] = self.Meta.model.USER
    #     elif role == 'moderator':
    #         ret['role'] = self.Meta.model.MODERATOR
    #     elif role == 'admin':
    #         ret['role'] = self.Meta.model.ADMIN
    #
    #     return ret


    # def get_role(self, obj):
    #     breakpoint()
    #     return obj.role[9:].split("'")[0]
    # role = serializers.ChoiceField(choices=YamdbUser.CHOICES)
    role = RoleField(choices=YamdbUser.CHOICES, default=YamdbUser.USER)

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
    # role = serializers.SerializerMethodField(read_only=True, source='get_role')

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'role',
                  ]
        lookup_field = 'username'


