from django.test import TestCase
import datetime
import pytz
from articles.scraper import NYTScraper
from articles.tagger import SportTagger
from articles.models import Article,Feed,Tag



# Create your tests here.

class ScraperTestCase(TestCase):
    
    # def test_scrape_static(self):
    #     """Test scraping a static xml file"""
    #     print("Found {} articles.".format(len(self.all_articles)))
    #     for item in self.all_articles:
    #         print("\t{} - {}".format(item["article_url"], item["article_title"]))
    #     self.assertEqual(len(self.all_articles),20)
    
    def test_scrape_pub_date(self):
        start_time = datetime.datetime.now()
        scraper = NYTScraper("http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
        scraper.scrape_all()
        for item in scraper.articles:
            self.assertTrue(item["pub_date"] < pytz.utc.localize(datetime.datetime.now()))
            
class TaggerTestCase(TestCase):
    
    def test_tag_baseball(self):
        st = SportTagger()
        feed = Feed(feed_url = "http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
        feed.save()
        feed.get_latest_articles()
        for article in feed.article_set.all():
            scores = st.get_tag_scores(article.article_text)
            # print("[{}] \t {}".format(scores["likeliest_tag"],article.article_title))
            self.assertTrue(scores["likeliest_tag"] == "Baseball")
            