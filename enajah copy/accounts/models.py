from django.db import models
from courses.models import Palier
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/')

class StudentProfile(models.Model):
    user = models.OneToOneField(User,related_name="user",on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    age = models.DateField(null=True,blank=True)
    
    photo = models.FileField(upload_to="profile_image/",blank=True)
    bio = models.TextField(default="",blank=True)
    facebook = models.URLField(default="",blank=True)
    school_name = models.CharField(max_length=200,default="",blank=True)
    palier = models.ForeignKey(Palier,on_delete=models.CASCADE,null=True,blank=True)

def create_profile(sender,**kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        student_profile=StudentProfile(user=user)
        student_profile.save()
post_save.connect(create_profile,sender=User)
