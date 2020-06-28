from django.contrib import admin
from blog.models import Postagem, Categoria

# Register your models here.

class PostagemAdmin(admin.ModelAdmin):
    pass


class CategoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Categoria, CategoriaAdmin)
