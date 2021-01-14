from users_api.models import YamdbUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = YamdbUser
        fields = ['username', 'first_name', 'last_name', 'email', ]
        lookup_field = 'username'
        extra_kwargs = {'url': {'lookup_field': 'username'}}
