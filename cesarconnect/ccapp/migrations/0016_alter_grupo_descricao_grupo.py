# Generated by Django 4.2.5 on 2023-10-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0015_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='descricao_grupo',
            field=models.TextField(default='descricao_grupo'),
            preserve_default=False,
        ),
    ]