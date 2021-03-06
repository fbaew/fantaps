from django.db import models
from django.utils import timezone
from articles.scraper import NYTScraper,TSNScraper,Scraper
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

    def __str__(self):
        return self.feed_url

    def get_latest_articles(self):
        self.log.debug("Getting latest articles for feed {}".format(self.feed_url))
        
        #gtl we need to somehow intuit the right scraper...
        #... I'm so sorry
        if "nytimes.com" in self.feed_url:
            scraper = NYTScraper(self.feed_url)
        elif "tsn.ca" in self.feed_url:
            scraper = TSNScraper(self.feed_url)

        scraper.scrape_all()
        for raw_article in scraper.articles:
            # print("Raw: {}".format(raw_article))
            a = Article()
            a.article_url = raw_article["article_url"]
            a.article_title = raw_article["article_title"]
            if not raw_article["pub_date"]:
                a.pub_date = timezone.now()
            else:
                a.pub_date = raw_article["pub_date"]
            a.parent_feed = self
            if len(Article.objects.all().filter(article_title=a.article_title)) == 0:
                print("[SCRAPING] '{}'".format(a.article_title))
                a.article_text = scraper.get_article_text(a.article_url)
                a.save()
            else:
                print("[CACHED] '{}'".format(a.article_title))

class Article(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    article_url = models.TextField(max_length=500)
    article_title = models.TextField(max_length=200)
    article_text = models.TextField(null=True)
    parent_feed = models.ForeignKey("Feed", default=get_default_feed)
    tagged = models.BooleanField(default=False)

    def __str__(self):
        return self.article_title
    

class Tag(models.Model):
    tag_name = models.TextField(max_length=50)
    tagged_articles = models.ManyToManyField(Article)
    
    def __str__(self):
        return self.tag_name
