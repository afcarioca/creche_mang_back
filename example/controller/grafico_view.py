from rest_framework.views import APIView
import json
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as pd
from example.model.aluno_model import AlunoModel
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class GraficoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    def post(self, request):
        data = json.loads(request.body)
        turma = data["turma"].upper()
        data =  AlunoModel.objects.filter(ativo=True).values()
        if turma != "TODAS":
          data = AlunoModel.objects.filter(turma=turma, ativo=True).values()
        
        if len(data) == 0:
           return HttpResponse(JsonResponse({'status': 'OK', 'message':'Lista Vazia!'}), content_type="application/json", status=200)

        dic_turma ={
           "nome":"",
           "qtd": 0,
           "sexo":{
              "Masculino":0,
              "Feminino":0
           },
           "bolsa_familia":{
              "Sim":0,
              "Não":0
           }
        }

        df = pd.DataFrame(data)   
        df = df.drop(columns=["id", "nome","ativo"])
        
        df.replace("B1", "Berçário 1", inplace=True)
        df.replace("B2", "Berçário 2", inplace=True)
        df.replace("M1", "Maternal 1", inplace=True)
        df.replace("M2", "Maternal 2", inplace=True)

        df.replace("M", "Masculino", inplace=True)
        df.replace("F", "Feminino", inplace=True)
        
        dic_turma["nome"] = turma.lower()
        dic_turma["qtd"] = int(len(df))
        dic_turma["sexo"]["Masculino"] = round((int(df["sexo"].value_counts().get("Masculino", 0))/dic_turma["qtd"])*100,1)
        dic_turma["sexo"]["Feminino"] = round((int(df["sexo"].value_counts().get("Feminino", 0))/dic_turma["qtd"])*100,1)
        dic_turma["bolsa_familia"]["Sim"] = round((int(df["bolsa_familia"].value_counts().get(True, 0))/dic_turma["qtd"])*100,1)
        dic_turma["bolsa_familia"]["Não"] = round((int(df["bolsa_familia"].value_counts().get(False, 0))/dic_turma["qtd"])*100,1)

       

        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Sucesso', "data":str(dic_turma)}), content_type="application/json", status=200)
        
     