# Generated by Django 3.0 on 2023-01-01 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20230101_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclassroom',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Classroom'),
        ),
    ]
