from django.core.management.base import BaseCommand
from django.utils import timezone
from articles.models import Article, Feed

class Command(BaseCommand):
    args = ""
    help = "scrape stuff and make articles from it..."

    def _populate(self):
        urls = [
        "http://rss.nytimes.com/services/xml/rss/nyt/Hockey.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml",
        "http://rss.nytimes.com/services/xml/rss/nyt/Golf.xml",
        "http://tsn.ca/nhl",
        "http://tsn.ca/nba",
        "http://tsn.ca/nfl",
        "http://tsn.ca/cfl",
        "http://tsn.ca/mlb",
        ]
        for url in urls:
            f = Feed()
            f.feed_url = url
            f.save()
        
    def handle(self, *args, **options):
        self._populate()

