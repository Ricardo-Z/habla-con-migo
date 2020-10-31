from django.db import models

# Create your models here.

class Service(models.Model):
     title = models.CharField(max_length=200, verbose_name="Título")
     subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
     content = models.TextField(verbose_name="Contenido")
     #image = models.ImageField(verbose_name="Imagen")
     image = models.CharField(max_length=200, verbose_name="Url de Video")
     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

     class Meta:
          verbose_name = "video"
          verbose_name_plural = "videos"
          ordering = ['-created']
     
     def __str__(self):
          return self.title

