# Generated by Django 4.2.7 on 2023-12-05 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_can', models.CharField(max_length=200)),
                ('descripcion_can', models.CharField(max_length=200)),
                ('url_can', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rec', models.CharField(max_length=200)),
                ('categoria_rec', models.CharField(max_length=200)),
                ('descripcion_rec', models.CharField(max_length=200)),
                ('url_rec', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usu', models.CharField(max_length=200)),
                ('email_usu', models.EmailField(max_length=200)),
                ('celular_usu', models.PositiveIntegerField()),
                ('fechanacimiento_usu', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='regalo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_reg', models.CharField(max_length=200)),
                ('descripcion_reg', models.CharField(max_length=200)),
                ('url_reg', models.CharField(max_length=200)),
                ('usuario_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]
