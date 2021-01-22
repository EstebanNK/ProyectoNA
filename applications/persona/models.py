from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields  import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name= 'Habilidad'
        verbose_name_plural= 'Habilidades empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad


class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'contador'),
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'otro'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombres completos', max_length=100, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default=0)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)


    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
    