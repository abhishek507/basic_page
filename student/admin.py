from django.contrib import admin

from .models import Student,Department,Subject,Examination

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Examination)
admin.site.register(Department)
# Register your models here.
