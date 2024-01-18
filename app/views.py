from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.
class listtodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer


class detail(generics.RetrieveUpdateAPIView):
        queryset = Todo.objects.all()
        serializer_class = Todoserializer

class create(generics.CreateAPIView):
        queryset = Todo.objects.all()
        serializer_class = Todoserializer

class delete(generics.DestroyAPIView):
        queryset = Todo.objects.all()
        serializer_class = Todoserializer

