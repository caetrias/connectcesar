# Generated by Django 4.2.5 on 2023-10-03 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0017_grupo_criador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='criador',
        ),
    ]