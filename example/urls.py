# example/urls.py
from django.urls import path
from example.views import index
from example.controller.login_view import LoginView
from example.controller.upload_view import UploadView
from example.controller.home_view import HomeView
from example.controller.register_view import RegisterView
from example.controller.aluno_view import AlunoView
from example.controller.grafico_view import GraficoView


urlpatterns = [
    path('', index),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/upload/", UploadView.as_view(), name="upload"),
    path("api/home/", HomeView.as_view(), name="home"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/form/", AlunoView.as_view(), name="form"),
    path("api/form/<int:id>/", AlunoView.as_view(), name="form"),
    path("api/grafico/", GraficoView.as_view(), name="grafico"),
    
]

