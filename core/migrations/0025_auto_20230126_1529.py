# Generated by Django 3.0 on 2023-01-26 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20230108_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclassroom',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Classroom'),
        ),
    ]