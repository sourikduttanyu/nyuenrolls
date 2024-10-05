from django.db import models

class user_info(models.Model):

    Edu_levels = [("Undergraduate","Undergraduate"),
                  ("Graduate","Graduate"),
                  ("PHD","PHD")]
    Schools = [("Tandon","Tandon"),
               ("Stern","Stern"),
               ("Tisch","Tisch"),
                ("Gallatin","Gallatin")]
    N_id = models.CharField(max_length=8,primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Education_Level = models.CharField(max_length=50,choices=Edu_levels)
    Phone_no = models.IntegerField(max_length=12)
    School = models.CharField(max_length=50,choices=Schools)
    ta= models.BooleanField()


class course_info(models.Model):
    ta = [("1","1"),("2","2"),("3","3")]

    course_id = models.CharField(max_length=11,primary_key=True)
    name = models.CharField()
    Instructor = models.CharField()
    course_Capacity = models.IntegerField(max_length=3)
    phd_course_capacity = models.IntegerField(max_length=3)
    #Establish a foreign key for User_info 
    # ta = models.ForeignKey(choices=ta)
    class_day = models.DateField()
    class_time = models.TimeField()
    students = models.ManyToManyField(user_info,)
    desciption = models.CharField(max_length=1000)
    credits = models.DecimalField(decimal_places=1,max_digits=3)

class faculty_info(models.Model):
    faculty_id = models.CharField(primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField(max_length=12)
    #Foreign keys to establish for
    # ta = models.ForeignKey(ta,)


class admin_info(models.Model):
    admin_id = models.CharField(primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField(max_length=12)
   



