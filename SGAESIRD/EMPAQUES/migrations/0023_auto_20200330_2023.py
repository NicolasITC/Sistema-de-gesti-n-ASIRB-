# Generated by Django 3.0.4 on 2020-03-30 23:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0022_mensaje_inicio_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_Turnos', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('emp01', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='01+', to='EMPAQUES.Usuario')),
                ('emp02', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='02+', to='EMPAQUES.Usuario')),
                ('emp03', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='03+', to='EMPAQUES.Usuario')),
                ('emp04', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='04+', to='EMPAQUES.Usuario')),
                ('emp05', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='05+', to='EMPAQUES.Usuario')),
                ('emp06', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='06+', to='EMPAQUES.Usuario')),
                ('emp07', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='07+', to='EMPAQUES.Usuario')),
                ('emp08', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='08+', to='EMPAQUES.Usuario')),
                ('emp09', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='09+', to='EMPAQUES.Usuario')),
                ('emp10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='10+', to='EMPAQUES.Usuario')),
                ('emp11', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='11+', to='EMPAQUES.Usuario')),
                ('emp12', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='12+', to='EMPAQUES.Usuario')),
                ('emp13', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='13+', to='EMPAQUES.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='lista_de_espera',
            name='rut',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Turnos',
        ),
    ]
