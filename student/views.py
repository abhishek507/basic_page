from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Examination,Department
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

# Create your views here.

def Home(request):

    return render(request,'index.html',{'name': request.GET.get('user','abhishek')})

#GET AND POST METHOD
@csrf_exempt
def student(request):
    if request.method == 'GET':
        age = request.GET.get('age')
        if age :
            stu_data = Student.objects.filter(stu_age=request.GET.get('age'))
        else:
            stu_data = Student.objects.all()
        print ('stu_date :',stu_data)

        return render(request, "student.html", {'data':stu_data})
    elif request.method == 'POST':
        data = eval(request.body)
        dept = Department.objects.get(dept_name=data['stu_dept'])
        data.update({"stu_dept":dept})
        resp = Student.objects.create(**data)
        return HttpResponse("success!")

        #data = eval(request.body)
        #dept = Department.objects.get(dept_name=data['stu_dept'])
        #data.update({'stu_dept':dept})
        #resp = Student.objects.create(**data)
        #return HttpResponse('success!')

#GET Method
def examination(request):
    print(request.method)
    name = request.GET.get('name')
    if name:
        stu_data = Examination.objects.filter(sub_name=request.GET.get('name'))
    else:
        stu_data = Examination.objects.all()
    print('stu_data :',stu_data)
    return render(request,'examination.html',{'data':stu_data})

#basic
#def examination(request):
    #stu_data = Examination.objects.all()
    #print('stu_data :',stu_data)
    #return render(request,'examination.html',{'data':stu_data})



#classbased views
#view
#Listview
#detailview
#createview
#deleteview
#updateview


class Studentview(ListView):
    model = Student
    template_name = "student_list.html"

class detaiview(DetailView):
    model = Student
    template_name = "student_detail.html"


class createview(CreateView):
    template_name = "student_form.html"

    model = Student
    fields = ['stu_name','stu_age','stu_dept','stu_gender']
    success_url = "/"

class stu_updateview(UpdateView):

    model = Student
    template_name = 'student_form.html'
    fields = ['stu_name','stu_age','stu_dept']
    success_url = '/'


