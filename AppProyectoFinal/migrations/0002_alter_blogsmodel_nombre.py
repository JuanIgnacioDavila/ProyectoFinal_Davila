# Generated by Django 4.1.7 on 2023-04-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsmodel',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
