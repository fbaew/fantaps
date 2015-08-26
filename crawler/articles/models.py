from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    pub_date = models.DateTimeField()
    article_url = models.TextField(max_length=500)
    article_title = models.TextField(max_length=200)

