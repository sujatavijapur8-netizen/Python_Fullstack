from django.urls import path
from  . import views
urlpatterns=[
    path("",views.login_page,name='login'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path('logout/',views.logout_page,name='logout'),
    path('students-form/',views.student_form,
         name='students_form'),
    path('students/',views.students_list,name='students_list'),
         
]

