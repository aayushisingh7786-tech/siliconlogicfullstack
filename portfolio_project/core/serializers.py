from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # List the specific fields to expose via the API
        fields = ['id', 'name', 'roll_no', 'course', 'joined_date']
