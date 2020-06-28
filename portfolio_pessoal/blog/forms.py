from django import forms

class ComentarioForm(forms.Form):
    autor = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Digite seu nome"}))
    comentario = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Digite aqui seu comentarios!"}))
