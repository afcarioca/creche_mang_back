# example/urls.py
from django.urls import path
from example.views import index
from example.controller.login_view import LoginView
from example.controller.upload_view import UploadView
from example.controller.home_view import HomeView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', index),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/upload/", UploadView.as_view(), name="upload"),
    path("api/home/", HomeView.as_view(), name="home")
]

