from django.http import HttpResponse
from rest_framework.views import APIView
import json
from example.validator.register_form import RegisterForm
from django.http import JsonResponse
from django.contrib.auth.models import User  

class RegisterView(APIView):

    def post(self, request):
        data = json.loads(request.body)
        form = RegisterForm(data)
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 

        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password1 = form.cleaned_data["password1"]
        password2 = form.cleaned_data["password2"]

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return HttpResponse(JsonResponse({'status': 'Erro', 'message':'O usuário já existe!'}), content_type="application/json", status=500)

        if password1 != password2:
            return HttpResponse(JsonResponse({'status': 'Erro', 'message':'Senhas Incompatíveis!'}), content_type="application/json", status=500)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=form.cleaned_data['password1']
        )

        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)
        
     
