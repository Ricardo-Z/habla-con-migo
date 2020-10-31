# Generated by Django 2.2.5 on 2020-10-31 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lectura', verbose_name='Imagen')),
                ('author', models.CharField(max_length=50, verbose_name='Autor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'lectura',
                'verbose_name_plural': 'lecturas',
                'ordering': ['-created'],
            },
        ),
    ]
