# Generated by Django 2.1.15 on 2023-12-06 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0004_diagnostics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crop',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='crop',
            name='planted_on',
        ),
    ]