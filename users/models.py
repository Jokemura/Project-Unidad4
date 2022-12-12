from django.db import models

# Create your models here.
class ProjectRegister(models.Model):
    
    title = models.CharField(max_length=50) 
    description =  models.TextField()
    tags = models.CharField(max_length=50)
    url = models.URLField(max_length=30)
    image = models.ImageField(upload_to='portfolio/images')

    def __str__(self):
        return self.title


