from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length = 20)
    def __str__(self):
            return str(self.empid)+" "+str(self.empname)
    
class Product(models.Model):
    proid = models.IntegerField()
    proname = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.proid)+" "+str(self.proname)
