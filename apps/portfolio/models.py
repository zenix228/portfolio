from django.db import models

class Portfolio(models.Model):
    'projects'
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d',)
    title = models.CharField(max_length=250)
    description = models.TextField()
    'experience'
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=500)
    about = models.TextField()
    'contact'
    image = models.ImageField()
    link = models.CharField(max_length=500)