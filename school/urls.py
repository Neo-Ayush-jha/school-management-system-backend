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
    path("manage-admission/",manageAdmission,name="manageAdmission"),
    path("manage-class/<int:id>/delete/",deleteClass,name="deleteClass"),
    path("manage-student/<int:id>/delete/",deleteStudent,name="deleteStudent"),
    path("manage-student/<int:id>/edit/",editStudent,name="editStudent"),
    path("single-student/<int:id>/",viewSingle,name="viewSingle"),
    path("approve-student/<int:id>/approve/",approve,name="approve"),
    path("manage/classes/view-class/<className>/",viewClassWise,name="viewClassWise"),
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
