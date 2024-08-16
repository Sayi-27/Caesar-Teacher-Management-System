from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'TSC_Number': 'TSC NUMBER',
         'first_name': 'FIRST NAME', 
         'last_name': 'LAST NAME',
         'Rensponsibility': 'RESPONSIBILITY',
         'Subject' : 'SUBJECT',
         'phone_number': 'PHONE NUMBER'
         }

        widgets = {
            'TSC_Number': forms.NumberInput(attrs={'class': 'form-control'}),
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control'}),
           'Rensponsibility': forms.TextInput(attrs={'class': 'form-control'}),
           'Subject ': forms.TextInput(attrs={'class': 'form-control'}),
           'phone_number': forms.NumberInput(attrs={'class': 'form-control'})
           }