from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from school_management.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="home"),
    path("apply/",applyForm,name="applyForm"),
    path("accounts/login/",login,name="login"),
    path("accounts/logout/",logout,name="logout"),
    path("manage-class/",manageClass,name="manageClass"),
    path("manage-student/",manageStudent,name="manageStudent"),
    path("manage-teacher/",manageTeacher,name="manageTeacher"),
    path("teacher/apply-form/",teacherApply,name="applyTeacherForm"),
    path("manage-admission/",manageAdmission,name="manageAdmission"),
    path("manage-new-teacher/",manageNewTeacher,name="manageNewTeacher"),
    path("manage-class/<int:id>/delete/",deleteClass,name="deleteClass"),
    path("manage-teacher/<int:id>/delete/",deleteTeacher,name="deleteTeacher"),
    path("manage-student/<int:id>/delete/",deleteStudent,name="deleteStudent"),
    path("manage-student/<int:id>/edit/",editStudent,name="editStudent"),
    path("manage-teacher/<int:id>/edit/",editTeacher,name="editTeacher"),
    path("single-student/<int:id>/",viewSingle,name="viewSingle"),
    path("single-teacher/<int:id>/",viewTeacher,name="viewTeacher"),
    path("approve-student/<int:id>/approve/",approve,name="approve"),
    path("approve-teacher/<int:id>/approve/",approveTeacher,name="approveTeacher"),
    path("manage/classes/view-class/<className>/",viewClassWise,name="viewClassWise"),
    path("manage/student/scan/",scanRfCode,name="scanRfCode"),
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
