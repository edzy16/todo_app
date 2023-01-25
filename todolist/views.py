# from django.shortcuts import render
# from .models import TodoList, categories

# # Create your views here.
# def Tasks(request):

#     todos = TodoList.objects.all()
#     categories = categories.objects.all()
    
#     if request.method == "POST":
#         if "taskAdd" in request.POST:
#             title = request.POST["description"]
#             date = str(request.POST["date"])
#             category = request.POST["category_select"]
#             content = title + "--" + date + " " + category
#             Todo = TodoList(title=title, content=content, due_date=date, category=categories.objects.get(name=category))
#             Todo.save()

#         if "taskDelete" in request.POST:
#             checkedlist = request.POST["checkedbox"]
#             for task in checkedlist:
#                 todo = TodoList.objects.get(id=int(task))
#                 todo.delete()
                
#     return render(request, "index.html", {"todos": todos, "categories": categories})

from django.shortcuts import render
from rest_framework import viewsets
from .models import TodoList, categories
from .serializers import TodoListSerializer, CategorySerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = CategorySerializer
