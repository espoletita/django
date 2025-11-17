from django.urls import path
from .views import listar_usuarios, novo_usuario, editar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios, name='usuarios'),
    path('usuarios/novo/', novo_usuario, name='usuarios_novo'),
    path('usuarios/<int:pk>/editar/', editar_usuario, name='editar_usuario'),
]
