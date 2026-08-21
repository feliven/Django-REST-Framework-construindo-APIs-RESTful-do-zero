from django.db import models


# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=False)
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.nome


class Curso(models.Model):
    OPCOES_NIVEL = [
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    ]

    codigo = models.CharField(max_length=10)
    descricao = models.TextField(
        blank=False,
    )
    nivel = models.CharField(
        max_length=1, blank=False, null=False, choices=OPCOES_NIVEL, default="B"
    )

    def __str__(self) -> str:
        return self.codigo
