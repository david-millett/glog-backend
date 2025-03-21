from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation, hashers

# Model
User = get_user_model()

# Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })
        password_validation.validate_password(password)
        data['password'] = hashers.make_password(password)
        return data

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirmation', 'first_name', 'last_name')