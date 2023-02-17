from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as loginfun,logout as logoutfunction
def homepage(r):
    return render(r,"index.html")
def applyForm(req):
    form=StudentForm(req.POST or None,req.FILES or None)
    if req.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
        else:
            return redirect(homepage)
    return render(req,"apply.html",{"form":form})
def login(req):
    LoginForm=AuthenticationForm(data = req.POST or None)
    if req.method == "POST":
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            if user is not None:
                print(user)
                loginfun(req,user)
                return redirect(homepage)
            else:
                return redirect(login)
    return render(req,"login.html",{'form':LoginForm})
def logout(req):
    logoutfunction(req)
    return redirect(login)
@login_required()
def manageStudent(req):
    data={}
    data['title'] = "Manage student"
    data['students']=Student.objects.filter(isApproved=True)
    return render(req, "admin/manageStudent.html",data)
@login_required()
def manageAdmission(req):
    data={}
    data['title'] = "Admission student"
    data['students']=Student.objects.filter(isApproved=False)
    return render(req, "admin/manageStudent.html",data)
@login_required()
def deleteStudent(req,id):
    std =Student.objects.get(pk=id)
    std.delete()
    return redirect(manageStudent)
@login_required
def editStudent(req,id):
    std = Student.objects.get(pk=id)
    form = StudentForm(req.POST or None,req.FILES or None ,instance=std)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageStudent)
    return render(req,"admin/editStudent.html",{"form":form})
@login_required
def viewSingle(req,id):
    std = Student.objects.get(pk=id)
    return render(req,"admin/SingleView.html",{"stu":std})
@login_required
def approve(req,id):
    stu=Student.objects.get(id=id,isApproved=False)
    stu.isApproved=True
    stu.save()
    return redirect(manageStudent)
@login_required
def manageClass(req):
    form = ClassForm(req.POST or None)
    data={}
    data['title'] = "Manage Class"
    data['form']=form
    if req.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(manageClass)
    data["classess"]=Classes.objects.all()
    return render(req,"admin/manageClass.html",data)
@login_required()
def deleteClass(req,id):
    cls=Classes.objects.get(pk=id)
    cls.delete()
    return redirect(manageClass)
@login_required()
def viewClassWise(r, className):
    data = {}
    data["title"] = "Manage " + className + " class students"
    data['students'] = Student.objects.filter(className__className = className, isApproved=True)
    return render(r, "admin/manageStudents.html", data)