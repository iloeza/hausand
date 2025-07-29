from django.db import models


class NivelChoices(models.TextChoices):
    MATERNA = "maternal"
    KINDER = "kinder"
    PRIMARIA = "primaria"
    SECUNDARIA = "secundaria"


class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    nivel = models.CharField(
        max_length=20, default=NivelChoices.KINDER, choices=NivelChoices.choices
    )
    alumno_responsable = models.CharField(max_length=100, blank=True)
    telefono_responsable = models.CharField(max_length=20, blank=True)
    email_responsable = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.title
