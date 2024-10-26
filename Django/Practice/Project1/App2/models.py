from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=20)
    empsalary = models.IntegerField()
    empaddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.empid)+" "+str(self.empname)+" "+str(self.empsalary)+" "+str(self.empaddress)

class Student(models.Model):
    
    sid = models.IntegerField()
    sname = models.CharField(max_length = 20)
    srank = models.IntegerField()

    def __str__(self):
        return str(self.sid)+" "+str(self.sname)+" "+str(self.srank)
