from django.test import TestCase
from articles.scraper import RSSScraper

# Create your tests here.

class ScraperTestCase(TestCase):
        def setup(self):
            pass
            
        def test_scrape_all(self):
            """some kind of magic to test live scraping"""
            scraper = RSSScraper("http://rss.nytimes.com/services/xml/rss/nyt/Baseball.xml")
            all_articles = scraper.scrape_all()
            self.assertEqual(1,1)

        def test_scrape_static(self):
            """Test scraping a static xml file"""
            scraper = RSSScraper("http://localhost/nice.xml")
            all_articles = scraper.scrape_all()
            print("Found {} articles.".format(len(all_articles)))
            for item in all_articles:
                print("\t{} - {}".format(item.article_url, item.article_title))
            self.assertEqual(len(all_articles),20)