# Generated by Django 4.2.7 on 2023-12-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pelicula'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciu', models.CharField(max_length=200)),
                ('descripcion_ciu', models.CharField(max_length=200)),
                ('url_ciu', models.CharField(max_length=200)),
            ],
        ),
    ]
