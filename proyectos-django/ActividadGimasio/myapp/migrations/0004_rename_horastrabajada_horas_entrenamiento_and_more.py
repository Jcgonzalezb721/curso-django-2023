# Generated by Django 4.2.7 on 2023-11-26 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_usuario_nuevo_remove_usuario_valor_x_hora_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HorasTrabajada',
            new_name='Horas_entrenamiento',
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='suscriptore',
        ),
    ]
