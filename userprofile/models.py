from django.db import models

class user_info(models.Model):
    Edu_levels = [("Undergraduate","Undergraduate"),
                  ("Graduate","Graduate"),
                  ("PHD","PHD")]
    Schools = [("Tandon","Tandon"),
               ("Stern","Stern"),
               ("Tisch","Tisch"),
               ("Gallatin","Gallatin")]
    
    N_id = models.CharField(max_length=8, primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Education_Level = models.CharField(max_length=50, choices=Edu_levels)
    Phone_no = models.IntegerField()
    School = models.CharField(max_length=50, choices=Schools)
    
    # A user can be a TA for one course
    ta_course = models.ForeignKey('course_info', null=True, blank=True, on_delete=models.SET_NULL)
    is_ta = models.BooleanField(default=False)
    
    # Many-to-Many relationship with courses
    course_enrolled = models.ManyToManyField('course_info')

class course_info(models.Model):
    course_id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    Instructor = models.OneToOneField('faculty_info', on_delete=models.CASCADE, related_name='course')
    course_Capacity = models.IntegerField()
    phd_course_capacity = models.IntegerField()
    class_day = models.DateField()
    class_time = models.TimeField()
    
    # Many-to-Many relationship for TAs
    ta_students = models.ManyToManyField(user_info, related_name='ta_students')
    students = models.ManyToManyField(user_info,related_name='course_enrolled')
    description = models.CharField(max_length=1000)
    credits = models.DecimalField(decimal_places=1, max_digits=3)

class faculty_info(models.Model):
    faculty_id = models.CharField(max_length=8, primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField()

    # A faculty can have multiple TAs (students)
    ta_students = models.ManyToManyField(user_info, related_name='faculty_tas')
    course = models.ManyToManyField(course_info,related_name="course_taught")
    


class admin_info(models.Model):
    admin_id = models.CharField(primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField(max_length=12)
   



