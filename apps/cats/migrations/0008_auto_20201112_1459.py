# Generated by Django 2.2.10 on 2020-11-12 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_cat_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat_images',
            old_name='property',
            new_name='cat',
        ),
    ]