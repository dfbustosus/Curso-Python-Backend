from django import forms
 
class CursoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    curso = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)