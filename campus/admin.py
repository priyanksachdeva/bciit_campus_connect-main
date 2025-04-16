from django.contrib import admin
from .models import Faculty,Student,Event 

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name','designation','department','email']
admin.site.register(Faculty,FacultyAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll_number','course','semester','email']
admin.site.register(Student,StudentAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','description','date','time','venue']
admin.site.register(Event,EventAdmin)