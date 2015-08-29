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
        
    def get_article_text(self,url):
        text = ""
        r = requests.get(url)
        page = BeautifulSoup(r.text,"html.parser")
        paragraphs = page.find_all("p")
        for p in paragraphs:
            text += p.text
        return text
        

class NYTScraper(Scraper):
    date_format = ""
    def __init__(self,url):
        super(NYTScraper,self).__init__(url)
        self.date_format = "%a, %d %b %Y %H:%M:%S %Z"

    def scrape_all(self):
        self.articles = []
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



        
class TSNScraper(Scraper):
    
    def scrape_all(self):
        self.articles = []
        r = requests.get(self.url)
        page = BeautifulSoup(r.text,"html.parser")
        articles_no_pics = page.findAll("article",{"class":"promo-no-image-related"})
        articles_pics = page.findAll("article",{"class":"promo-image"})
        articles_on_page = articles_no_pics + articles_pics
        i=0
        for item in articles_on_page:
            print ("Trying item {}".format(i))
            i+=1
            a = {}
            a["pub_date"] = None

            try:
               a["article_title"] = item.find(class_="headline").find("h2").text
               a["article_url"] = self.url + item.find(class_="headline").find("a")["href"]
               print("Success: {}".format(a["article_title"]))
               print(item)

            except AttributeError as error:
                print("Problem with this: ~~~~~~~\n{}\n\n~~~~~~".format(item))
                a["article_title"] = item.find(class_="headline-super").find("h2").text
                a["article_url"] = self.url + item.find(class_="headline-super").find("a")["href"]
           
            self.articles.append(a)