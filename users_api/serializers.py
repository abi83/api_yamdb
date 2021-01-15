from users_api.models import YamdbUser
from rest_framework import serializers


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


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        ret['role'] = ret['role']
        return ret


    # def get_role(self, obj):
    #     breakpoint()
    #     return obj.role[9:].split("'")[0]
    # role2 = serializers.ChoiceField(choices=YamdbUser.CHOICES)
    # role = serializers.SerializerMethodField(read_only=True, source='get_role')

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'role',
                  ]
        lookup_field = 'username'


