from rest_framework import serializers
from .models import Trainee

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'username', 'track', 'is_active', 'is_staff']

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = Trainee(**validated_data)
        if password:
            user.set_password(password)  # Hash password
        user.save()
        return user