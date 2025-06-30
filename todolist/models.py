from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('AF', 'A FAZER'),
        ('EM', 'FAZENDO'),
        ('FN', 'FINALIZADO'),
    ]

    titulo = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AF')

    def __str__(self):
        return self.titulo
