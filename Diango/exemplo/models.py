from django.db import models

# Create your models here.
class Tarefa(models.Model):
    no_tarefa    = models.CharField(max_length=200)
    st_status    = models.CharField(max_length=1)
    dt_inclusao  = models.DateTimeField('data cadastro', default=None, null=True, blank=True)
    dt_alteracao = models.DateTimeField('data alteracao', default=None, null=True, blank=True)
