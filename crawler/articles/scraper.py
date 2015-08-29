import requests
import datetime
import pytz
#from articles.models import Article
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self,url):
        self.url = url
        self.articles = []

    def scrape_all_articles(self):
        r = requests.get(self.url)
        

class RSSScraper(Scraper):
    date_format = ""
    def __init__(self,url):
        super(RSSScraper,self).__init__(url)
        self.date_format = "%a, %d %b %Y %H:%M:%S %Z"

    def scrape_all(self):
        r = requests.get(self.url)
        feed = BeautifulSoup(r.text, "lxml")
        items = feed.find_all("item")
        for item in items:
            a = {}
            a["article_url"] = item.find_all("link")[0].nextSibling
            a["article_title"] = item.find_all("title")[0].string
            naive_date = datetime.datetime.strptime(item.find_all("pubdate")[0].string,
                                            self.date_format)
            a["pub_date"] = pytz.utc.localize(naive_date)
            
            self.articles.append(a)


    def get_article_text(self,url):
        text = ""
        r = requests.get(url)
        page = BeautifulSoup(r.text,"html.parser")
        paragraphs = page.find_all("p")
        for p in paragraphs:
            text += p.text
        return text