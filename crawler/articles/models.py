from django.db import models
from django.utils import timezone
import logging


# Create your models here.

def get_default_feed():
    '''

    Dummy method to return our bogus feed... 
    probably can do better than just returning 3.

    '''
    return 3#    return Feed.objects.get(pk=3)



class Feed(models.Model):
    last_ripped = models.DateTimeField(null=True)
    feed_url = models.TextField(max_length=500)
    log = logging.getLogger(__name__)

    def get_latest_articles(self):
        self.log.debug("Getting latest articles for feed {}".format(self.feed_url))


class Article(models.Model):
    
    pub_date = models.DateTimeField()
    article_url = models.TextField(max_length=500)
    article_title = models.TextField(max_length=200)
    parent_feed = models.ForeignKey("Feed", default=get_default_feed)


