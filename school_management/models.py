from django.db import models

GENDER =(
    ("M","male"),
    ("F","female"),
    ("O","other")
)
ClassList=(
    ("PLAY","PLAY"),
    ("LKG","LKG"),
    ("UKG","UKG"),
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
)
SubjectName=(
    ("English","English"),
    ("Maths","Maths"),
    ("Hindi","Hindi"),
    ("Science","Science"),
    ("S.St","S.St"),
    ("Sanskrit","Sanskrit"),
    ("Computer","Computer"),
    ("Drawing","Drawing"),
    ("P.T","P.T"),
    ("Evs","Evs"),
    ("G.k","G.k"),
    ("Urdu","Urdu"),
    ("Hindi Grammer","Hindi Grammer"),
    ("English Grammer","English Grammer"),
)
MONTHS = (
    ("jan","january"),
    ("feb","feb"),
    ("march","march"),
    ("april","april"),
    ("may","may"),
    ("june","june"),
    ("july","july"),
    ("aug","aug"),
    ("sep","sep"),
    ("oct","oct"),
    ("nov","nov"),
    ("dec","dec"),
)
# Create your models here.
class Classes(models.Model):
    class_name=models.CharField(max_length=100,choices=ClassList)
    def __str__(self):
        return self.class_name
    
class Student(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    father_name=models.CharField(max_length=150)
    address=models.TextField()
    gender=models.CharField(max_length=10,choices=GENDER)
    nationality=models.CharField(max_length=150,choices=(("Indian","Indian"),("Other","Other")))
    city=models.CharField(max_length=150,choices=(("Purnea","Purnea"),("Pune","Pune")))
    state=models.CharField(max_length=150,choices=(("Bihar","Bihar"),("Punjab","Punjab")))
    pin_code=models.IntegerField()
    contact=models.IntegerField()
    image=models.ImageField(upload_to="photo/",null=True,blank=True)
    dob = models.DateField(help_text="use MM/DD/YYYY format")
    className=models.ForeignKey("Classes",on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)
    rf_code= models.CharField(max_length=100,default=None,blank=True,null=True,unique=True)
    def __str__(self):
        return self.first_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100,choices=SubjectName)
class Teacher(models.Model):
    t_name = models.CharField(max_length=150)
    t_contact = models.IntegerField()
    t_email = models.EmailField()
    t_dob=models.DateField(help_text="use MM/DD/YYYY format")
    t_address = models.TextField()
    isApproved = models.BooleanField(default=False)
    salary = models.IntegerField(max_length=100, default=None,blank=True,null=True,)
    t_gender=models.CharField(max_length=10,choices=GENDER)
    t_subject = models.ForeignKey("Subject",on_delete=models.CASCADE,default=None,blank=True,null=True,unique=True)
    def __str__(self):
        return self.t_name

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=200, choices=MONTHS)
    date_of_payment = models.DateField(auto_now=False, null=True,blank=True)
    status = models.BooleanField(default=False)
    amount = models.IntegerField(default=1000)

    def __str__(self):
        return self.student.first_name + " - " + self.month