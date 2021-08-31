from django.db import models


class usuario(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    espiracion = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return '{0},{1}'.format(self.owner,self.espiracion)

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200)

    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)
