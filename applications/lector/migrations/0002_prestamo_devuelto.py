# Generated by Django 3.1.3 on 2020-11-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='devuelto',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]