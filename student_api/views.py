from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from app.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from     rest_framework.permissions import IsAuthenticated
from rest_framework import response

class api_student(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = student_serializer
    #permission_classes = [IsAuthenticated]

class api_student_ind(RetrieveUpdateDestroyAPIView):
    #queryset = Student.objects.all()
    serializer_class = student_serializer
    permission_classes = [IsAuthenticated]
    context_object_name = "students"
    
    def get_object(self):     #to get only orders related to the authenticated user
        return Student.objects.get(user=self.request.user)

                                            #get object was used because it's a single student report we want to see and 
                                            #the report is there profil