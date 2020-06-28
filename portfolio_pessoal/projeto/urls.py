from django.urls import path
from . import views

urlpatterns = [
    path("", views.projeto_index, name="projeto_index"),
    path("<int:pk>/", views.projeto_detail, name="projeto_detail"),
]
