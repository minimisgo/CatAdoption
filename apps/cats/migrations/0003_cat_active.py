# Generated by Django 2.2.10 on 2020-11-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20201108_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
