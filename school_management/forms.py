# from django.forms import ModelForm,Form,CharField,PasswordInput
from django.forms import ModelForm
from .models import *
class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude =("isApproved","rf_code")
        
class EditStudentForm(ModelForm):
    class Meta:
        model = Student
        exclude =("isApproved",)
        
# class loginForm(Form):
#     username =  CharField(max_length=120)
#     password = CharField(max_length=150,widget=PasswordInput())
class ClassForm(ModelForm):
    class Meta:
        model =Classes
        fields="__all__"