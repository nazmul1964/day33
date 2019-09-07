from django.shortcuts import render, redirect
from .models import Employee
from less4App.forms import EmployeeForm

from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def index(request):
    emp = Employee.objects.all()

    context = {'title': 'Welcome', 'employees': emp}
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert successfully ')
                return redirect('/')
            except Exception as e:
                print("type error: " + str(e))
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES) #try
    return render(request,'edit.html',{'employee':employee,'form':form})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,request.FILES,instance=employee)
    if form.is_valid():
        try:
            form.save()
            messages.error(request,'Update successfully ')
            return redirect('/')
        except Exception as e:
                print("type error: " + str(e))
    else:
        messages.error(request,form.errors)
        
    return render(request, 'edit.html', {'employee': employee,'form':form})
