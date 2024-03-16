"""
URL configuration for basic_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import Home,student,examination,Studentview,detaiview,createview,stu_updateview

urlpatterns = [
    path('', Home),
    path('student/',student),
    path('student/examination/',examination),
    path('student1/',Studentview.as_view()),
    path('student1/<pk>/',detaiview.as_view()),
    path('student_add/',createview.as_view()),
    path('student1/<pk>/student_edit/',stu_updateview.as_view()),
    path('admin/', admin.site.urls),
]
