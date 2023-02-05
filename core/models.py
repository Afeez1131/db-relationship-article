from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user_profile', null=True)
    phone = models.CharField(max_length=11)
    age = models.PositiveIntegerField()

    # def __str__(self):
    #     return f'{self.user.username} profile'


class Classroom(models.Model):
    name = models.CharField(max_length=100, unique=True)


# class StudentClassroom(models.Model):
#     student = models.CharField(max_length=100)
#     classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


class StudentClassroom(models.Model):
    student = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, related_name='student_classroom', null=True)


class Person(models.Model):
    name = models.CharField(max_length=100)


# class Event(models.Model):
#     name = models.CharField(max_length=150)
#     person = models.ManyToManyField(Person)


class Event(models.Model):
    name = models.CharField(max_length=150)
    person = models.ManyToManyField(Person, related_name='events')
