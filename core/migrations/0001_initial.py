# Generated by Django 3.0 on 2023-01-01 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentClassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='core.Classroom')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_classroom', to='core.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('age', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
