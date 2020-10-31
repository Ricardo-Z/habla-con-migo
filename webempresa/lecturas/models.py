from django.db import models
from django.utils.timezone import now
# Create your models here.

class Lectura(models.Model):
     title = models.CharField(max_length=200, verbose_name="Título")
     content = models.TextField(verbose_name="Contenido")
     published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
     #image = models.ImageField(verbose_name="Imagen", upload_to="lectura", null=True, blank=True)
     image = models.FileField(verbose_name="PDF", upload_to='lectura')
     author = models.CharField(max_length=50, verbose_name = "Autor")
     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

     class Meta:
          verbose_name = "lectura"
          verbose_name_plural = "lecturas"
          ordering = ['-created']
     
     def __str__(self):
          return self.title
