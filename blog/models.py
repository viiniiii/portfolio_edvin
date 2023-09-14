from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_created=True)
    description = models.TextField(max_length=3500)
    image = models.ImageField(upload_to='blog/images/', blank=True)

    def __str__(self):
        return self.title