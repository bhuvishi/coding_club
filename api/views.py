from django.shortcuts import render
from rest_framework import generics
from api.models import Student
from api.serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
