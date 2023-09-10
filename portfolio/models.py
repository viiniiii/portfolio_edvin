from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)