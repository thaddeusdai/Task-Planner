from django.urls import path
from . import views


urlpatterns = [
path('<_username>/', views.get_data, name="data"),
]