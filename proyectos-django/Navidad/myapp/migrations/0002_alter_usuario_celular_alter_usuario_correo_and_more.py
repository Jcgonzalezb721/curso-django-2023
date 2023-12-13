# Generated by Django 4.2.7 on 2023-12-03 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.PositiveBigIntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Regalos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decripcion', models.CharField(default='', max_length=200)),
                ('url', models.CharField(default='', max_length=200)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]
