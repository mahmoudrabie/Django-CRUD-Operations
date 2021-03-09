from django import forms
from .models import Employee

from django.utils.translation import gettext_lazy as _


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': _('Full Name'),
            'mobile': _('Full Name'),
            'emp_code': _('EMP.Code'),
            'position': _('Position'),

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
