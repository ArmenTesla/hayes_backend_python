from rest_framework import serializers
from .models import CustomUser
from .utils import generate_password 

class RegisterModelSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ['username','age']


    def create(self, validated_data):
        password = generate_password(validated_data['username'])
        user = CustomUser(**validated_data)
        user.set_password(password)  
        user.save()
        self._generated_password = password
        return user

class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['img']