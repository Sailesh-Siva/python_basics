from django.contrib import admin

# Register your models here.

from .models import Employee
from .models import Student
#admin.site.register(Employee)
admin.site.register(Student)
@admin.register(Employee)




class Employeetest(admin.ModelAdmin):
    list_display = ('empid','empname','empsalary','empaddress',)
    list_filter = ('empsalary',)
    ordering = ('empname',)
    search_fields = ('empname',)


