from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    telefone = models.CharField(max_length=12)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"nome: {self.nome}, cpf: {self.cpf}, e-mail: {self.email},  telefone: {self.telefone},  data nascimento: {self.data_nascimento}" 
