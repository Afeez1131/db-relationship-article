# Generated by Django 3.0 on 2023-01-07 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20230107_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclassroom',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Classroom'),
        ),
    ]
