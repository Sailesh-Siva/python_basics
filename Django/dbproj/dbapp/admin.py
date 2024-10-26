from django.contrib import admin
from .models import Employee
# Register your models here.

#admin.site.register(Employee) # only firtst time user registeration

@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display = ('empid','empname','empsalary','empaddress')
    list_filter = ('empsalary',)
    ordering=('empname',)
    search_fields=('empname',)
