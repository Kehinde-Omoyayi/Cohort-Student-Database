from app.models import *
from rest_framework import serializers

class student_serializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','matric_num',
        'department','current_level','level_duration','admission_year']
        #to make certain things only readable
        read_only_fields = ['matric_num', 'current_level', 'admission_year']