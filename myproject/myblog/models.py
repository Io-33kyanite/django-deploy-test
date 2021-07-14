from django.db import models
from mdeditor.fields import MDTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to = 'media/')
    body = MDTextField()

    def __str__(self):
        return self.title