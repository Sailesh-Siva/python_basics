from django.contrib import admin
from .models import Product,Employee
# Register your models here.

#admin.site.register(Employee)
#admin.site.register(Product)

@admin.register(Employee)

class Employeecl(admin.ModelAdmin):
    list_display = ('empid','empname',)
    list_filter = ('empid',)
    ordering = ('empid',)
    search_fields = ('empid',)
    

