from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.



class Video(models.Model):
    title = models.CharField(max_length=200)
    embed_code = models.TextField()
    video_slug = models.SlugField(blank=True,unique=True)

    def save(self, *args, **kwargs):
        self.video_slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
