# Generated by Django 2.2.5 on 2019-11-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191112_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Category', verbose_name='Categorias'),
        ),
    ]
