from django.http import HttpResponse
from rest_framework.views import APIView
from example.model.aluno_model import AlunoModel
from example.validator.aluno_form import AlunoForm
import json
from django.http import JsonResponse


class AlunoView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        form = AlunoForm(data)
        
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 
       
        nome = form.cleaned_data["nome"]
        turma = form.cleaned_data["turma"]
        sexo = form.cleaned_data["sexo"]
        bolsa_familia = form.cleaned_data["bolsa_familia"]

        if  isinstance(bolsa_familia, bool) or isinstance(turma, bool) or isinstance(sexo, bool):
            return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação'}),  content_type="application/json", status= 400) 
 
        if AlunoModel.objects.filter(nome=nome).exists():
            return HttpResponse(JsonResponse({'status': 'Erro', 'message':'O aluno já existe!'}), content_type="application/json", status=400)

        aluno = AlunoModel.objects.create(
            nome = nome,
            turma = turma.upper(),
            bolsa_familia= bolsa_familia,
            sexo = sexo.upper(),
        )
        aluno.save()
        return HttpResponse(JsonResponse({'status': 'OK', 'message':'Aluno registrado!'}), content_type="application/json", status=200)

    def get(self, request):
        data = json.loads(request.body)
        turma = data["turma"].upper()
        data = AlunoModel.objects.all().values()
        if turma != "TODAS":
          data = AlunoModel.objects.filter(turma=turma).values()
        json_data = json.dumps(list(data))
        alunos =json.loads(json_data)
        return HttpResponse(JsonResponse({"status": "OK", "message": "Lista de Alunos!", "data":alunos}), content_type="application/json", status=200)

    def put(self, request, id):
        data = json.loads(request.body)
        form = AlunoForm(data)

          
        if not form.is_valid():
           errors = dict(form.errors.items())
           return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação', 'errors': errors}),  content_type="application/json", status= 400) 
       
        nome = form.cleaned_data["nome"]
        turma = form.cleaned_data["turma"]
        sexo = form.cleaned_data["sexo"]
        bolsa_familia = form.cleaned_data["bolsa_familia"]

        if  isinstance(bolsa_familia, bool) or isinstance(turma, bool) or isinstance(sexo, bool):
            return HttpResponse(JsonResponse({'status': 'Erro', 'message': 'Erros de Validação'}),  content_type="application/json", status= 400) 
 
        if not AlunoModel.objects.filter(id=id).exists():
            return HttpResponse(JsonResponse({'status': 'Erro', 'message':'O aluno não existe!'}), content_type="application/json", status=400)


        aluno= AlunoModel.objects.get(id=id)
        aluno.nome = nome
        aluno.turma = turma.upper()
        aluno.bolsa_familia = bolsa_familia
        aluno.sexo = sexo.upper()
        aluno.save()

        return HttpResponse(JsonResponse({"status": "OK", "message": "Aluno Atualizado!"}), content_type="application/json", status=200)