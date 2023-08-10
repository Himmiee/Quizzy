from rest_framework import serializers
from .models import Detail, Course, Option


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title"]

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    course = CourseSerializer()
    class Meta:
        model = Detail
        fields = ["id", "question", "answer", "created", "updated","course", "options"]