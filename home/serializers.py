from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'dept',
            'roll'
        ]

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.dept = validated_data.get('dept', instance.dept)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #
    #     instance.save()
    #     return instance





