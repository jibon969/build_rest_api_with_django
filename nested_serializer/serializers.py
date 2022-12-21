from rest_framework import serializers
from .models import Profile, Hobby


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = [
            'user',
            'name',
            'description',
            'status'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Hobby.objects.create(**validated_data)
        for user in user_data:
            Profile.objects.create(user=user, **user)
        return user