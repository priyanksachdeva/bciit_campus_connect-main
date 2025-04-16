from django.shortcuts import render

# Create your views here.

from .models import Faculty, Student, Event
def home(request):
    return render(request, 'campus/base.html')
    
def dashboard(request):
    return render(request, 'campus/dashboard.html')

def faculty_info(request):
    faculties = Faculty.objects.all()
    return render(request, 'campus/faculty.html', {'faculties': faculties})

def student_info(request):
    students = Student.objects.all()
    return render(request, 'campus/student.html', {'students': students})

def event_info(request):
    events = Event.objects.all()
    return render(request, 'campus/events.html', {'events': events})