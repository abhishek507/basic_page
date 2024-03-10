from django.contrib import admin

from .models import Student,Department,Subject,Examination,marks

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Examination)
admin.site.register(Department)
admin.site.register(marks)
# Register your models here.
