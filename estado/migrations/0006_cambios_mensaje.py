# Generated by Django 3.2.7 on 2021-10-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0005_alter_cambios_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambios',
            name='mensaje',
            field=models.CharField(blank=True, max_length=255, verbose_name='mensaje'),
        ),
    ]
