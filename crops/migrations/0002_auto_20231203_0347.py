# Generated by Django 2.1.15 on 2023-12-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
