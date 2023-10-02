# Generated by Django 4.2.5 on 2023-10-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0004_pessoa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='nome',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='idade',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='senha',
            field=models.TextField(default='senha', max_length=255),
            preserve_default=False,
        ),
    ]