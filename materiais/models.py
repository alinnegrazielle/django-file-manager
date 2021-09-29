from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Arquivo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='pdf/')

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.descricao, self.categoria.nome)
