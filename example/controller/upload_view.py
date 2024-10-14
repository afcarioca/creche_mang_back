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
from django.core import serializers

class UploadView(APIView):
  

    def post(self, request):
        file_obj = request.FILES["xlsx"]
        df = pd.read_excel(file_obj)
        df = df.drop(columns=["Professora", 'Carimbo de data/hora', "nome"]) 

        df.replace("Berçário", "bercario", inplace=True)
        df.replace("Maternal 1", "maternal1", inplace=True)
        df.replace("Maternal 2", "maternal2", inplace=True)
      
        
        variaveis = ["total", "bercario", "maternal1", "maternal2"]
        dic = { "total": {"nome":"Total","qtd":0, "sexo": {"masculino": 0,"feminino": 0},"bolsa":{"sim":0,"nao":0},"alcool":{ "sim":0,"nao":0}},
            "bercario":  {"nome":"Berçário","qtd":0, "sexo": {"masculino": 0,"feminino": 0},"bolsa":{"sim":0,"nao":0},"alcool":{"sim":0,"nao":0}},
            "maternal1": {"nome":"Maternal 1", "qtd":0, "sexo": {"masculino": 0,"feminino": 0},"bolsa":{"sim":0,"nao":0},"alcool":{"sim":0,"nao":0}},
            "maternal2": {"nome":"Maternal 2", "qtd":0, "sexo": {"masculino": 0,"feminino": 0},"bolsa":{"sim":0,"nao":0},"alcool":{"sim":0,"nao":0}},
          }
        for valor in variaveis:
            df_aux = df.copy()
            if valor != "total":
                df_aux = df_aux[df_aux["turma"] == valor]
            dic[valor]["qtd"] = len(df_aux)

            
        
            dic[valor]["sexo"]["masculino"] = len(df_aux[df_aux["sexo"] == "Masculino"])
            dic[valor]["sexo"]["feminino"] = len(df_aux[df_aux["sexo"] == "Feminino"])
            
            dic[valor]["bolsa"]["sim"] = len(df_aux[df_aux["bolsa"] == "Sim"])
            dic[valor]["bolsa"]["nao"] = len(df_aux[df_aux["bolsa"] == "Não"])
            
            dic[valor]["alcool"]["sim"] = len(df_aux[df_aux["alcool"] == "Sim"])
            dic[valor]["alcool"]["nao"] = len(df_aux[df_aux["alcool"] == "Não"])


        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', "data":str(dic)}), content_type="application/json", status=200)
        
     