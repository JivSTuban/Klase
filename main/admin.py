from django.contrib import admin

# Register your models here.
from .models import Student, Instructor, Course, Department, Assignment, Announcement

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)
