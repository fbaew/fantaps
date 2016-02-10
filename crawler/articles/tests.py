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
        print("Testing that NYT Scraper only returns articles from the past")
        start_time = datetime.datetime.now()
        scraper = NYTScraper("http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
        scraper.scrape_all()
        for item in scraper.articles:
            self.assertTrue(item["pub_date"] < pytz.utc.localize(datetime.datetime.now()))
            
class TaggerTestCase(TestCase):
    
    def dumb_test_tag_baseball(self):

        """
        In theory, every article from this feed should get tagged as baseball.
        This isn't really a unit test though, and would be better in some kind
        of performance testing suite; I'm not sure that pulling from an
        unknown outside source is a recipe for successful unit tests.

        Maybe add this back to the suite when our tagging mechanism is smarter
        """

        st = SportTagger()
        feed = Feed(feed_url = "http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
        feed.save()
        feed.get_latest_articles()
        for article in feed.article_set.all():
            scores = st.get_tag_scores(article)
            print("[{}] \t {}".format(scores["likeliest_tag"],article.article_title))
            self.assertTrue(scores["likeliest_tag"] == "Baseball")

    def test_sporttagger_case_insensitive(self):
        """
        We should count each instance of the sport name regardless of its case.
        """
        print("Testing sport tagger for case-insensitivity")
        article = Article(
            pub_date = pytz.utc.localize(datetime.datetime.now()),
            article_url = "http://gregglewis.net/fakeurl",
            article_title = "Coach disgraced in counterfeit helmet scandal",
            article_text = "basEball baseball baseball basketball basketball",
            parent_feed = Feed(feed_url = "http://gregglewis.net/fake.xml"),
            tagged = False
        )

        tagger = SportTagger()
        result = tagger.get_tag_scores(article)
        self.assertTrue(result["likeliest_tag"] == "Baseball")
        self.assertTrue(result["scores"][result["likeliest_tag"]] == 3)
