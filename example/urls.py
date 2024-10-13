# example/urls.py
from django.urls import path
from example.views import index
from example.controller.login_view import LoginView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index),
    path("api/login/", LoginView.as_view(), name="login")
]

