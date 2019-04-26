from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'phone_number', 'first_name', 'last_name', 'date_joined')
