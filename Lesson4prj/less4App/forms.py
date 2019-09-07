from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
                'dob' : forms.DateInput(attrs={'class': 'datepicker1 form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email Address'}),
                'salary': forms.TextInput(attrs={'class': 'form-control'}),

    	}

        dob = forms.DateField(
            widget=forms.DateInput(format='%Y/%m/%d'),input_formats=('%Y/%m/%d', )
        )
