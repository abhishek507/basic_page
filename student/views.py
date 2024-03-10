from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def Home(request):
    return render(request,'index.html')

def student(request):
    stu_data = Student.objects.all()
    print ('stu_date :',stu_data)
    return render(request,'student.html',{'data':stu_data})



