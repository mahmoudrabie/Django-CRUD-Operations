from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

# Create your views here.
def translate(language='ar', message=''):
    cur_language = get_language()
    try:
        activate(language)
        translated_msg = _(message)
    finally:
        activate(cur_language)
    return translated_msg

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    trans = {
        'submit': _('Submit')
    }
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form, 'trans': trans})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
