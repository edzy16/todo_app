from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todolist.views import TodoViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'todolist', TodoViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

