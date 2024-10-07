from django.db import models

class StudentInfo(models.Model):
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
    ta_course = models.ForeignKey('CourseInfo', null=True, blank=True, on_delete=models.SET_NULL)
    is_ta = models.BooleanField(default=False)
    course_enrolled = models.ManyToManyField('CourseInfo', related_name='enrolled_students')

class CourseInfo(models.Model):
    course_id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    Instructor = models.OneToOneField('FacultyInfo', on_delete=models.SET_NULL, related_name='course', null=True)
    course_Capacity = models.IntegerField()
    phd_course_capacity = models.IntegerField()
    class_day = models.DateField()
    class_time = models.TimeField()
    ta_students = models.ManyToManyField(StudentInfo, related_name='ta_students')
    description = models.CharField(max_length=1000)
    credits = models.DecimalField(decimal_places=1, max_digits=3)

class FacultyInfo(models.Model):
    faculty_id = models.CharField(max_length=8, primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField()
    ta_students = models.ManyToManyField(StudentInfo, related_name='faculty_tas')
    courses_taught = models.ManyToManyField(CourseInfo, related_name="instructors")

class AdminInfo(models.Model):
    admin_id = models.CharField(primary_key=True)
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone_no = models.IntegerField(max_length=12)