from django import forms
from jsonschema import ValidationError

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=200)
    turma = forms.CharField(max_length=20)
    sexo = forms.CharField(max_length=20)
    bolsa_familia = forms.IntegerField(required=True)


    def clean_sexo(self):
        sexo = self.cleaned_data.get("sexo")
        if sexo not in("m", "f"):
            return False
        return sexo

    def clean_turma(self):
        turma = self.cleaned_data.get("turma")
        if turma not in ("b1","b2", "m1", "m2"):
            return False
        return turma 

    def clean_bolsa_familia(self):
        bolsa_familia = self.cleaned_data.get("bolsa_familia")
        if bolsa_familia not in (0, 1):
            return False
        return bolsa_familia