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
