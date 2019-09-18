# Generated by Django 2.2.2 on 2019-08-29 20:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0004_anotaciones_categoria_anotaciones_finanzas_turnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id_Anuncios', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Universidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Lista_de_Espera',
            fields=[
                ('id_Lista_de_Espera', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('carrera', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=12)),
                ('universidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Universidades')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_Comentarios', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('contenido', models.TextField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Anuncios')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='anuncios',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Usuario'),
        ),
    ]