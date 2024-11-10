from rest_framework.views import APIView
import json
from django.http import HttpResponse
from example.validator.login_form import LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from django.contrib.auth.models import User


class PerfilView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    def post(self, request):
        data = json.loads(request.body)
        print(data)

      
        
        
        usuario = User.objects.filter(username=data["username"]).first()
        if usuario is None:
            return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Usuário não existe'}),  content_type="application/json", status= 400) 
  
        dados_usuario = {
            "nome": usuario.username,
            "email": usuario.email,
        }
     
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', 'data':dados_usuario}), content_type="application/json", status=200)
    