from django.contrib import admin
from .models import StudentID, Student, Department

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentID)




