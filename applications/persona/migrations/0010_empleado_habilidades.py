# Generated by Django 3.1.4 on 2021-01-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0009_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
