from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser
from django.contrib.auth.models import Group

def listar_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'pages/usuarios/list.html', {
        'page_title': 'Usuários',
        'usuarios': usuarios,
    })

def novo_usuario(request):
    grupos = Group.objects.all()
    if request.method == 'POST':
        # pega dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('password')
        grupo_id = request.POST.get('grupo')

        senha_hash = make_password(senha)
        usuario = CustomUser(
            nome=nome,
            email=email,
            telefone=telefone,
            cpf=cpf,
            password=senha_hash
        )
        usuario.save()

        # vincula o grupo único
        grupo = Group.objects.get(id=grupo_id)
        usuario.groups.set([grupo])

        return redirect('usuarios')
    else:
        return render(request, 'pages/usuarios/edit.html', {'user_form': CustomUser(), 'grupos': grupos})

def editar_usuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    grupos = Group.objects.all()
    selected_grupo_id = usuario.groups.first().id if usuario.groups.exists() else None

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.cpf = request.POST.get('cpf')
        senha = request.POST.get('password')
        if senha:
            usuario.password = make_password(senha)
        usuario.save()

        grupo_id = request.POST.get('grupo')
        grupo = Group.objects.get(id=grupo_id)
        usuario.groups.set([grupo])

        return redirect('usuarios')
    else:
        context = {'user_form': usuario, 'grupos': grupos, 'selected_grupo_id': selected_grupo_id}
        return render(request, 'pages/usuarios/edit.html', context)