from django.shortcuts import render
from blog.models import Postagem, Comentario
from blog.forms import ComentarioForm

# Create your views here.

def blog_index(request, template_name="blog_index.html"):
    postagens = Postagem.objects.all().order_by("-criada_em")
    context = {"postagens": postagens}
    return render(request, template_name, context)


def blog_category(request, categoria, template_name="blog_category.html"):
    postagens = Postagem.objects.filter(categoria__name__contains=categoria).order_by("-criada_em")
    context = {"categoria": categoria, "postagens": postagens}
    return render(request, template_name, context)


def blog_detail(request, pk, template_name="blog_detail.html"):
    postagem = Postagem.objects.get(pk=pk)

    formulario = ComentarioForm()
    if request.method == "POST":
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = Comentario(autor=formulario.cleaned_data["autor"], comentario=formulario.cleaned_data["comentario"], postagem=postagem)
            comentario.save()

    comentarios = Comentario.objects.filter(postagem=postagem)
    context = {"postagem": postagem, "comentarios": comentarios, "formulario": formulario}
    return render(request, template_name, context)

