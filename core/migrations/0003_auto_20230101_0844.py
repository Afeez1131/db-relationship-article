# Generated by Django 3.0 on 2023-01-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230101_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclassroom',
            name='student',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
