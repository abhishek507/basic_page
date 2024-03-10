from django.db import models

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    desc = models.TextField()
    dept_HOD = models.CharField(max_length=50)
    staff_count = models.IntegerField()
    Tot_sub = models.IntegerField()

    class Meta:
        db_table = 'Department'

    def __str__(self):
        return self.dept_name



class Student(models.Model):

    stu_name = models.CharField(max_length=100,null=True)
    stu_age = models.IntegerField()
    stu_dept = models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    stu_gender = models.CharField(choices=(('male','MALE'),('female','FEMALE')),max_length=20)

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return self.stu_name





class Subject(models.Model):
    sub_code = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return self.sub_name


class Examination(models.Model):
    exam_duration = models.FloatField(default=180)
    Tot_marks = models.FloatField(default=100)
    sub_code = models.ForeignKey(Subject,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)


    class Meta:
        db_table = 'Examination'

    def __str__(self):
        return self.sub_name



class marks(models.Model):

    stu_name = models.ForeignKey(Student,on_delete=models.CASCADE,)
    stu_sub = models.CharField(max_length=50,null=True,)
    stu_marks = models.IntegerField()

    class Meta:
        db_table = "marks"

    def __str__(self):
        return str(self.stu_name)
