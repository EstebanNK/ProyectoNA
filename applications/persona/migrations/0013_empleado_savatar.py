# Generated by Django 3.1.4 on 2021-01-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0012_auto_20210107_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='savatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
