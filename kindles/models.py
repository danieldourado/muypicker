from django.db import models
import datetime

# Create your models here.
class Modelo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Negociacao(models.Model):
    modelo              = models.ForeignKey(Modelo)
    preco_de_compra     = models.DecimalField(max_digits=6, decimal_places=2  )
    numero_de_parcelas  = models.IntegerField(default=1)
    data_de_compra      = models.DateField(default = datetime.date.today)
    preco_de_venda      = models.DecimalField(max_digits=6, decimal_places=2, )
    data_de_venda       = models.DateField(null = True)

