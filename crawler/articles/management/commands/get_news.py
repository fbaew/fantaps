from django.core.management.base import BaseCommand
from django.utils import timezone
from articles.models import Article

class Command(BaseCommand):
    args = ""
    help = "scrape stuff and make articles from it..."

    def _populate(self):

        for i in range(10):
            a = Article()
            a.article_url = "http://gregglewis.net/test/{}".format(i)
            a.article_title = "Gregg's Article #{}".format(i)
            a.pub_date = timezone.now()
            a.save()

    def handle(self, *args, **options):
        self._populate()

