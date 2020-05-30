from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', LoginView.as_view(), name = "login"),
    path('logout/', views.logout_request, name = 'logout'),
    path('forgotpassword/', views.forgot_password, name="forgot_password"),
    path('resetpassword/<_username>', views.reset_password, name='reset_password')
]