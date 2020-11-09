# Generated by Django 2.2.17 on 2020-11-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cat_images/%Y/%m/%D/')),
            ],
        ),
    ]