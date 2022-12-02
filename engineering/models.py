from django.db import models

# Create your models here.
class NoticeBoard_Engineering(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField( max_length=250)
    date = models.DateField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title


class Events(models.Model):
    Title = models.CharField( max_length=50)
    discription = models.CharField( max_length=10000)
    Image = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None)
    Image2 = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None,blank=True)
    Image3 = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None,blank=True)
    Image4 = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None,blank=True)
    Image5 = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None,blank=True)
    Image6 = models.ImageField(upload_to='static/img/Engineeringimage', height_field=None, width_field=None, max_length=None,blank=True)
    date = models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.Title
    
class Faculty(models.Model):
    name  = models.CharField( max_length=50)
    image = models.ImageField( upload_to='static/img/Engineeringimage/Faculty', height_field=None, width_field=None, max_length=None)
    qualification = models.TextField()
    description =models.CharField( max_length=50,null=True)
    Designation = models.CharField( max_length=50,null=True)
    Email = models.EmailField(max_length=254)
    Teaching_Experience = models.IntegerField(null=True)
    Industry_Experience = models.IntegerField(null=True)
    Research_Experience = models.IntegerField(null=True)
    

    def __str__(self):
        return self.name


