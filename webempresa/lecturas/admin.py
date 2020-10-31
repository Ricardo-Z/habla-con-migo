from django.contrib import admin
from .models import Lectura
# Register your models here.

class LecturaAdmin(admin.ModelAdmin):
     readonly_fields = ('created', 'updated')
     ordering = ('author', 'published') #si se desea solo un campo de ordenamiento, se dja solo uno con una coma al final
     date_hierarchy = 'published'


admin.site.register(Lectura, LecturaAdmin)