from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Django ko batao kis table ke liye form chahiye
        fields = ['name', 'uni', 'subject', 'semester']  # Kaun kaun se dabbe (inputs) chahiye