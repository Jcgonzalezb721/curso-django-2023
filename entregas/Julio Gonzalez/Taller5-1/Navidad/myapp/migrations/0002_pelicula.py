# Generated by Django 4.2.7 on 2023-12-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pel', models.CharField(max_length=200)),
                ('descripcion_pel', models.CharField(max_length=200)),
                ('url_pel', models.CharField(max_length=200)),
            ],
        ),
    ]
