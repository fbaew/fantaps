import requests
import datetime
import pytz
#from articles.models import Article
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

    def overlaps(self,list1,list2):
        for item in list1:
            if item in list2:
                return True
        return False
    
    def scrape_all(self):
        self.articles = []
        r = requests.get(self.url)
        page = BeautifulSoup(r.text,"html.parser")
        unfiltered_articles = page("article")
        
        '''
        Get the bulk of the articles from the page...
        '''
        articles = list(
            filter(
                lambda x: "normal" not in x["class"] and "three-column" not in x["class"]
                , unfiltered_articles
            )
        )
        
        for article in articles:
            a = {}
            a["pub_date"] = None
            generic_classes = ["promo-image-related","promo-image","promo-no-image-related"]
            
            #First we scrape the top story.
            if "super-promo" in article["class"]: #the big article up top
                try:
                    a["article_title"] = article.find("h2").text
                except AtrributeError as e:
                    print("Couldn't find article title...")
                    
                try:
                    article_rel = article.find(class_="headline-super").find("a")["href"]
                    a["article_url"] = urljoin(self.url,  article_rel)

                except AttributeError as e:
                    print("Couldn't retrieve article link for [{}]".format(a["article_title"]))
                    f = open("scraper/ref/debug.html","w")
                if "article_title" in a.keys() and "article_url" in a.keys():
                    self.articles.append(a)
            
            elif self.overlaps(generic_classes, article["class"]) == True:
                try:
                    a["article_title"] = article.find("h3").text
                except AttributeError as e:
                    print("Error retrieving article title.")
                
                try:
                    article_rel = article.find(class_="headline").find("a")["href"]
                    a["article_url"] = urljoin(self.url, article_rel)
                except AttributeError as e:
                    print("Couldn't get url for [{}]".format(a["article_title"]))
                if "article_title" in a.keys() and "article_url" in a.keys():
                    self.articles.append(a)            

        '''
        TSN displays a row of three stories which we may or may not care about...
        We need different logic to extract their details.
        '''
        extra_stories = page(class_="three-column")

