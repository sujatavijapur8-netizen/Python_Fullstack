from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def student_form(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('students_list')

    else:
        form = StudentForm()

    return render(
        request,
        'Students/students_form.html',
        {'form': form}
    )


def students_list(request):

    students = Student.objects.all()

    return render(
        request,
        'students/students_list.html',
        {'students': students}
    )
def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
            return redirect('dashboard')

        else:
            return render (request, "students/login.html", {
                'error' : "Inavalid Username or password"
            }) 


    return render(request, 'students/login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'students/dashboard.html')

def logout_page(request):

    if request.method == "POST":
        logout(request)

    return redirect('login')