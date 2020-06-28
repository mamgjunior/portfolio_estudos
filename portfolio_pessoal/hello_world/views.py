from django.shortcuts import render

# Create your views here.

def hello_world(request, template_name="hello_world.html"):
    return render(request, template_name, {})
