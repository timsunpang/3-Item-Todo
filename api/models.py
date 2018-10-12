from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class DateTimeBase(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class AbstractTodoList(DateTimeBase):
	def __str__(self):
		return self.created.strftime('%m/%d/%Y')

	class Meta:
		abstract = True

class TodoList(AbstractTodoList):
	pass

class OtherItemList(AbstractTodoList):
	pass

class AbstractTodo(DateTimeBase):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return '{0}: {1}'.format(self.title, self.completed)

	class Meta:
		abstract = True

class Todo(AbstractTodo):
	todolist = models.ForeignKey('TodoList', on_delete=models.CASCADE)

class OtherTodo(AbstractTodo):
	otheritemlist = models.ForeignKey('OtherItemList', on_delete=models.CASCADE)

class DayEntry(DateTimeBase):
	todolist = models.OneToOneField(TodoList, on_delete=models.CASCADE)
	otheritemlist = models.OneToOneField(OtherItemList, on_delete=models.CASCADE)
	data = JSONField()

class User(AbstractUser, DateTimeBase):
	data = JSONField()