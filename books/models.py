from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    nivel = models.CharField(max_length=20, default='kinder')
    responsable = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
