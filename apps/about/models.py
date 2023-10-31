from django.db import models

class About(models.Model):
    name = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.name

class Skills(models.Model):
    skills_image = models.ImageField()
    skills_name = models.CharField(max_length=205)
    
    def __str__(self):
        return self.skills_name