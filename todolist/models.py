from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Categories")
        verbose_name_plural = ("Categories")
        
    def __str__(self):
        return self.name
    
class TodoList(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.title