from django.test import TestCase
import datetime
from articles.scraper import RSSScraper

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
        scraper = RSSScraper("http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
        scraper.scrape_all()
        for item in scraper.articles:
            self.assertTrue(item["pub_date"] < datetime.datetime.now())
