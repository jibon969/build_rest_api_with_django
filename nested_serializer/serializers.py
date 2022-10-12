from rest_framework import serializers
from .models import Profile, Hobby


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_hobby = HobbySerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_hobby = validated_data.pop('user_hobby')
        profile_instance = Profile.objects.create(**validated_data)
        for hobby in user_hobby:
            Hobby.objects.create(user=profile_instance, **hobby)
        return profile_instance
