from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('<_username>/', views.todo, name="todo"),
    path('delete/<task_id>/<_username>', views.delete, name = "delete"),
    path('post/<task_id>', views.post, name="post"),
]