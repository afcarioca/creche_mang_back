from rest_framework.views import APIView
import json
from django.http import HttpResponse
from example.validator.login_form import LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class LoginView(APIView):
    
    def post(self, request):
        data = json.loads(request.body)
        form = LoginForm(data)
     
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 
       
        user = authenticate(username=data["usuario"],password=data["senha"])
        
        if user is None:
                return HttpResponse(JsonResponse({'status': 'Acesso Negado', 'message':'Usuário Inexistente'}), content_type="application/json", status=403)
        
        refresh = RefreshToken.for_user(user)
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso','Refresh':str(refresh),'Token':str(refresh.access_token)}), content_type="application/json", status=200)
        
     