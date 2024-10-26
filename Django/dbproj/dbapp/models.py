from django.db import models

# Create your models here.
class Employee():
    empid = models.IntegerField()
    empname = models.CharField(max_length = 20)
    empsalary = models.IntegerField()
    empaddress = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.empid)+" "+self.empname+" "str(self.empsalary)+" "+self.empaddress
    
