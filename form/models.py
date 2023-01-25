from django.db import models

class ModelUpload(models.Model):
    tipo = models.CharField(max_length=4)
    data = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.IntegerField()
    cartao = models.IntegerField()
    hora = models.DateTimeField(auto_now_add=True)
    dono_da_loja = models.CharField(max_length=50)
    nome_da_loja = models.CharField(max_length=50)
