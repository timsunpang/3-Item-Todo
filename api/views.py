from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Todo, TodoList, OtherItemList, OtherTodo, DayEntry
from api.serializers import TodoSerializer, TodoListSerializer, OtherTodoSerializer, OtherItemListSerializer, DayEntrySerializer
from rest_framework import generics

# Create your views here.
class TodoIndex(generics.ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

class OtherTodoIndex(generics.ListCreateAPIView):
	queryset = OtherTodo.objects.all()
	serializer_class = OtherTodoSerializer

class OtherTodoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OtherTodo.objects.all()
	serializer_class = OtherTodoSerializer

class TodoListIndex(generics.ListCreateAPIView):
	queryset = TodoList.objects.all()
	serializer_class = TodoListSerializer

class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = TodoList.objects.all()
	serializer_class = TodoListSerializer

class OtherItemListIndex(generics.ListCreateAPIView):
	queryset = OtherItemList.objects.all()
	serializer_class = OtherItemListSerializer

class OtherItemListDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OtherItemList.objects.all()
	serializer_class = OtherItemListSerializer

class DayEntryIndex(generics.ListCreateAPIView):
	queryset = DayEntry.objects.all()
	serializer_class = DayEntrySerializer

class DayEntryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DayEntry.objects.all()
	serializer_class = DayEntrySerializer