from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# from courses.models import Module
# Create your models here.

class Quiz(models.Model):
    title=models.CharField(max_length=200)
    #module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name="related_module",blank=True,null=True)
    quiz_slug = models.SlugField(blank=True,unique=True)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(default=0)
    pourcentage = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def add_one(self):
        self.score+=1
        return self.score
    def total_score(self,total_score):

        self.pourcentage = round(total_score/self.number_of_questions * 100)
        return self.pourcentage

    def save(self, *args, **kwargs):
        self.quiz_slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('courses:quiz_detail', kwargs={"quiz_slug":self.quiz_slug})
    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTIONS_TYPE=(
        ('qcm',"Choix Multiple"),
        ("tf","Faux ou Vrais"),
        ("text","Reponse a text"),
    )
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="related_question")
    order = models.IntegerField(default=0)
    question_type = models.CharField(max_length=20,choices=QUESTIONS_TYPE)
    question_text = models.TextField()


    def __str__(self):
        return "{} ?".format(self.question_text)
class Indice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE,related_name="related_indice")
    indice_text = models.CharField(max_length=400)
    def __str__(self):
        return self.indice_text
class Answer(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE,related_name="related_answer")
    answer_text=models.CharField(max_length=200)
    correct = models.BooleanField(default = False)
    def __str__(self):
        return self.answer_text
