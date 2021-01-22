# Generated by Django 3.1.4 on 2021-01-06 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='departamento',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='job',
            field=models.CharField(choices=[('0', 'contador'), ('1', 'administrador'), ('2', 'economista'), ('3', 'otro')], max_length=1, verbose_name='Trabajo'),
        ),
    ]
