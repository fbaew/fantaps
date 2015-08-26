from django.db import models
from django.utils import timezone

# Create your models here.

def get_default_feed():
    return 3#    return Feed.objects.get(pk=3)



class Feed(models.Model):
    last_ripped = models.DateTimeField(null=True)
    feed_url = models.TextField(max_length=500)

    def get_latest_articles(self):
        pass


class Article(models.Model):
    
    pub_date = models.DateTimeField()
    article_url = models.TextField(max_length=500)
    article_title = models.TextField(max_length=200)
    parent_feed = models.ForeignKey("Feed", default=get_default_feed)


