from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    author = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={"id": self.id})
