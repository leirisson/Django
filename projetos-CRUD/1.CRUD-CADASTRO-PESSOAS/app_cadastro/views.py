from django.shortcuts import render, redirect
from app_cadastro.models import Pessoa
# Create your views here.

def home(requests):
    # pegando as pessoas cadastradas no banco de dados e passando para o template
    pessoas = Pessoa.objects.all()
    return render(requests, "app_cadastro/pages/home.html", {"pessoas": pessoas})


# cadastrar uma pessoa 
def cadastro(request):

    # obtendo dados do formulario de cadastro
    campo_nome = request.POST.get("nome")
    campo_cpf = request.POST.get("cpf")
    campo_email = request.POST.get("email")
    campo_telefone = request.POST.get("telefone")
    campo_data_nascimento = request.POST.get("data_nascimento")

    # criando uma pessoa no banco de dados
    Pessoa.objects.create(nome=campo_nome, cpf=campo_cpf, email=campo_email, telefone=campo_telefone, data_nascimento=campo_data_nascimento)
    pessoas = Pessoa.objects.all()

    # o contexto fornecido deve ser um dicionario 
    return render(request, "app_cadastro/pages/home.html", {"pessoas":pessoas})



#atualizando um cadastro
def update(request, id_usuario):
    pessoa = Pessoa.objects.get(id=id_usuario)

    # passando o contexto 
    return render(request, "app_cadastro/pages/update.html", {"pessoa":pessoa})

def editado(request, id_usuario):

    novo_nome = request.POST.get("nome")
    novo_cpf = request.POST.get("cpf")
    novo_email = request.POST.get("email")
    novo_telefone = request.POST.get("telefone")
    nova_data_nascimento = request.POST.get("data_nascimento")

    # recuperando o usuario pelo id_usuario
    pessoa_cadastrada = Pessoa.objects.get(id=id_usuario)

    #passando os novos dados 
    pessoa_cadastrada.nome = novo_nome
    pessoa_cadastrada.cpf = novo_cpf
    pessoa_cadastrada.email = novo_email
    pessoa_cadastrada.telefone = novo_telefone
    pessoa_cadastrada.data_nascimento = nova_data_nascimento

    #salvando no banco de dados as alterações
    pessoa_cadastrada.save()

    return redirect(home)

#deletando um cadastro
def deletar(request, id_usuario):
    pessoa = Pessoa.objects.get(id=id_usuario)
    pessoa.delete()
    return redirect(home)
