from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    Nombres=models.CharField(max_length=100,verbose_name="Nombre(s)")
    fecha_nacimiento=models.DateField(verbose_name='Fecha de Nacimiento',null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name='Fecha de Ingreso',null=False,blank=False)

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"

    def __str__(self) -> str:
        return self.Nombres


class Frase(models.Model):
    comentario=models.TextField(verbose_name='Comentario',max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Frase'
        verbose_name_plural = 'Frases'

    def __str__(self) -> str:
        return self.comentario