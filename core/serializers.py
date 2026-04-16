from rest_framework import serializers
from .models import Student, teachers # Tumhare models yahan import honge

# 1. Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # Wo saari fields jo tum ne models.py mein banayi hain
        fields = ['id', 'name', 'uni', 'subject', 'semester', 'image']

# 2. Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teachers
        fields = ['id', 'name', 'uni', 'subject']