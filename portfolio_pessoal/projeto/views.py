from django.shortcuts import render
from projeto.models import Projeto

# Create your views here.

def projeto_index(request, template_name="projeto_index.html"):
    projetos = Projeto.objects.all()
    context = {"projetos": projetos}
    return render(request, template_name, context)


def projeto_detail(request, pk, template_name="projeto_detalhes.html"):
    projeto = Projeto.objects.get(pk=pk)
    context = {"projeto": projeto}
    return render(request, template_name, context)
