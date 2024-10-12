# example/urls.py
from django.urls import path
from example.views import index
from example.controller.login_view import LoginView


urlpatterns = [
    path('', index),
    path("api/login", LoginView.as_view(), name="login")
]