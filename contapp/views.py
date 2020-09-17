from django.shortcuts import render
from .models import Employee
from .form import EmpForm
from django.http.response import HttpResponse

# Create your views here.

def emp_view(request):
    if request.method == "POST":
        eform = EmpForm(request.POST)
        if eform.is_valid():
            ename1 = request.POST.get('ename')
            salary1 = request.POST.get('salary')
            email1 = request.POST.get('email')
            mobile1 = request.POST.get('mobile')
            location1 = request.POST.get('location')

            data = Employee(
                ename = ename1,
                salary = salary1,
                email = email1,
                mobile = mobile1,
                location= location1
            )

            data.save()
            eform = EmpForm()
            context = {'form':eform}
            return render(request,'contact.html',context)
    else:
        eform = EmpForm()
        context = {'form':eform}
        return render(request,'contact.html',context)
        