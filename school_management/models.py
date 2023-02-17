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
    dob=models.DateField()
    className=models.ForeignKey("Classes",on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name