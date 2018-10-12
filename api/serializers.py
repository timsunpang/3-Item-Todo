from rest_framework import serializers
from api.models import Todo, TodoList, OtherTodo, OtherItemList, DayEntry

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'title', 'description', 'completed', 'todolist', 'created', 'last_modified')

class OtherTodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OtherTodo
		fields = ('id', 'title', 'description', 'completed', 'otheritemlist', 'created', 'last_modified')

class TodoListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoList
		fields = ('created', 'last_modified')

class OtherItemListSerializer(serializers.ModelSerializer):
	class Meta:
		model = OtherItemList
		fields = ('created', 'last_modified')

class DayEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = DayEntry
		fields = ('data', 'created', 'last_modified')