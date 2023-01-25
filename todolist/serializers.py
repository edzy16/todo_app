from rest_framework import serializers
from .models import TodoList, categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ('id', 'name')
        
class TodoListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'content', 'created', 'due_date', 'category')
