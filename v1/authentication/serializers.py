from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'bio')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        return user

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'bio')
        read_only_fields = ('email',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'name', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password'],
            # bio=validated_data.get('bio', '')
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()