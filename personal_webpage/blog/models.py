from django.db import models
from datetime import date

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField(default = date.today())
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title