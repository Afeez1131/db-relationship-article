from django.contrib import admin
from .models import Profile, Student, Classroom, StudentClassroom, Person, Event
# Register your models here.


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(StudentClassroom)
admin.site.register(Person)
admin.site.register(Event)

