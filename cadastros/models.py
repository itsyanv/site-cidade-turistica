from django.db import models

# Create your models here.

class Estado(models.Model):
    nmEstado = models.CharField(max_length=100, verbose_name="Estado")
    ufEstado = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return "{}-{}".format(self.nmEstado, self.ufEstado)
    
class Cidade(models.Model):
    nmCidade = models.CharField(max_length=100, verbose_name="Cidade")
    dddCidade = models.CharField(max_length=2, verbose_name="DDD")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    def __str__(self):
        return "{}, {}-{}".format(self.nmCidade, self.estado.nmEstado, self.estado.ufEstado)

class Ponto(models.Model):
    nmPonto = models.CharField(max_length=100, verbose_name="Ponto Turístico")
    hrInicio = models.TimeField(verbose_name="Abertura")
    hrfim = models.TimeField(verbose_name="Encerramento")
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor do Ingresso")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    def __str__(self):
        return "{} - {}, {}-{}".format(self.nmPonto, self.cidade.nmCidade, self.cidade.estado.nmEstado, self.cidade.estado.ufEstado)