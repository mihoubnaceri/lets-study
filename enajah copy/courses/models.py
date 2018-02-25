from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from videos.models import Video
from quizzes.models import Quiz

class Palier(models.Model):
    title = models.CharField(max_length=200)
    palier_slug = models.SlugField(blank=True,unique=True)


    def save(self, *args, **kwargs):
        self.palier_slug = slugify(self.title)
        super(Palier, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('courses:palier_detail', kwargs={"palier_slug":self.palier_slug})
class Module(models.Model):
    palier = models.ForeignKey(Palier,on_delete=models.CASCADE,related_name="related_module")
    title = models.CharField(max_length=200)
    #durer = models.CharField(max_length=70,default="0 Weeks")
    description = models.TextField(blank=True)
    module_slug = models.SlugField(blank=True,unique=True)
    def save(self, *args, **kwargs):
        self.module_slug = slugify(self.title)
        super(Module, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('courses:module_detail', kwargs={"module_slug":self.module_slug})
#class Course()
TRIMESTRE = (
    ("t1","Trimestre 1"),
    ("t2","Trimestre 2"),
    ("t3","Trimestre 3"),
)
class Course(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name="related_course")
    title = models.CharField(max_length=200)
    trimestre = models.CharField(max_length=20,choices=TRIMESTRE)
    course_slug = models.SlugField(unique=True,blank=True)
    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.title+"-"+self.trimestre)
        super(Course, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={"course_slug":self.course_slug})
    def __str__(self):
        return self.title

class Tutorial(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="related_tutorial")
    title = models.CharField(max_length=200)
    tutorial_slug = models.SlugField(blank=True,unique=True)
    video = models.ForeignKey(Video,on_delete=models.CASCADE,null=True,blank=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.tutorial_slug = slugify(self.title)
        super(Tutorial, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('courses:tutorialst', kwargs={"tutorial_slug":self.tutorial_slug})
    def __str__(self):
        return self.title
