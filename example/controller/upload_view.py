from rest_framework.views import APIView
import json
from django.http import HttpResponse
from example.validator.login_form import LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd


class UploadView(APIView):
    def post(self, request):
        file_obj = request.FILES["xlsx"]
        df = pd.read_excel(file_obj)
        print(df)
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso'}), content_type="application/json", status=200)
        
     