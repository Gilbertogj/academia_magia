# Generated by Django 5.0.4 on 2024-05-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('identificacion', models.CharField(max_length=10)),
                ('edad', models.PositiveIntegerField()),
                ('afinidad_magica', models.CharField(choices=[('Oscuridad', 'Oscuridad'), ('Luz', 'Luz'), ('Fuego', 'Fuego'), ('Agua', 'Agua'), ('Viento', 'Viento'), ('Tierra', 'Tierra')], max_length=20)),
                ('estatus', models.CharField(choices=[('En revisión', 'En revisión'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='En revisión', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tipo_trebol_grimorio', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
