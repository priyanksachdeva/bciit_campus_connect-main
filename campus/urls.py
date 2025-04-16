from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Nested under dashboard
    path('dashboard/faculty/', views.faculty_info, name='faculty_info'),
    path('dashboard/students/', views.student_info, name='student_info'),
    path('dashboard/events/', views.event_info, name='event_info'),

    # Optional: Also allow flat routes
    path('faculty/', views.faculty_info),
    path('students/', views.student_info),
    path('events/', views.event_info),
]
