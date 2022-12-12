from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=150)
    decription = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date= models.DateField(datetime.date.today)
