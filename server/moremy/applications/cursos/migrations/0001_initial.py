# Generated by Django 2.1.1 on 2020-09-12 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('nivel_dificultad', models.IntegerField()),
                ('ultima_actualizacion', models.DateField(verbose_name='Ultima actualización')),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Duración')),
                ('status_progreso', models.CharField(choices=[('P', 'Por Iniciar'), ('C', 'En Curso'), ('F', 'Finalizado')], max_length=1, verbose_name='Status de Progreso')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.Curso')),
            ],
        ),
    ]