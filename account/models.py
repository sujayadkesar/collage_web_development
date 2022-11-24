from django.db import models

# Create your models here.
COLLEGE_choice = (
    ('select','select'),
    ('INSTITUTE OF ALLIAD HEALTH SCIENCES','INSTITUTE OF ALLIAD HEALTH SCIENCES'),
    ('INSTITUTE OF ENGINEERING AND TECHNOLOGY','INSTITUTE OF ENGINEERING AND TECHNOLOGY'),
    ('INSTITUTE OF MANAGEMENT AND COMMERCE','INSTITUTE OF MANAGEMENT AND COMMERCE'),
    ('INSTITUTE OF COMPUTER SCIENCE & INFORMATION SCIENCE','INSTITUTE OF COMPUTER SCIENCE & INFORMATION SCIENCE'),
    ('INSTITUTE OF SOCIAL SCIENCES & HUMANITIES','INSTITUTE OF SOCIAL SCIENCES & HUMANITIES'),
    ('INSTITUTE OF NURSING SCIENCE','INSTITUTE OF NURSING SCIENCE'),
    ('INSTITUTE OF PHYSIOTHERAPY','INSTITUTE OF PHYSIOTHERAPY'),
    ('INSTITUTE OF HOTEL MANAGEMENT & TOURISM',"INSTITUTE OF HOTEL MANAGEMENT & TOURISM"),
    ('INSTITUTE OF EDUCATION','INSTITUTE OF EDUCATION')
)

department_choice = (
    ('select','select'),
    ('CS Department', 'CS Department'),
    ('E&C Department','E&C Department'),
    ('Mechanical Department','Mechanical Department'),
    ('Civil Department','Civil Department'),
    ('AI&ML Department','AI&ML Department'),
    ('Robotics and AIML Department','Robotics and AIML Department'),
    ('MBA','MBA'),
    ('Material Science and Engineering','Material Science and Engineering')
)

class Profile(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    PICTURE = models.ImageField( upload_to='static/profilephoto', default='static/img/team/download.png')
    COLLEGE = models.CharField(choices=COLLEGE_choice,default='select',max_length=200)
    DEPARTMENT = models.CharField(choices=department_choice,max_length=200,default='select')
    USN_Number = models.CharField( max_length=50)
    year = models.IntegerField()
    
    def __str__(self):
        return self.USN_Number

