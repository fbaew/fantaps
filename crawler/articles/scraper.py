"""
Provides different variations of a core Scraper class, to extract news
articles from known sites.
"""

import requests
import datetime
import pytz
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Scraper():
    """
    Generic scraper. Not itself ever instatiated.
    """
    def __init__(self, url):
        self.url = url
        self.articles = []
        request = requests.get(self.url)
        self.content = BeautifulSoup(request.text, "html.parser")

#    def scrape_all_articles(self):
#        r = requests.get(self.url)

    def get_article_text(self, url):
        """
        Naively pull all text from a given web page. In many cases, this will
        probably be overridden by each subclass, but for now, since we are
        just doing frequency analysis and looking for a few key words, it's
        okay to just rip all the <p> tags.
        """
        text = ""
        request = requests.get(url)
        paragraphs = self.content.find_all("p")
        for paragraph in paragraphs:
            text += paragraph.text
        return text

class NYTScraper(Scraper):
    """
    Rip articles from the New York Times sports section
    """
    date_format = ""
    def __init__(self, url):
        super(NYTScraper, self).__init__(url)
        request = requests.get(self.url)
        self.content = BeautifulSoup(request.text, "lxml")
        self.date_format = "%a, %d %b %Y %H:%M:%S %Z"

    def scrape_all(self):
        """
        Extract article details (headline, URL, and date) from each item found
        at self.url
        """

        items = self.content.find_all("item")
        for item in items:
            details = {}
            details["article_url"] = item.find_all("link")[0].nextSibling
            details["article_title"] = item.find_all("title")[0].string
            naive_date = datetime.datetime.strptime(
                item.find_all("pubdate")[0].string,
                self.date_format)
            details["pub_date"] = pytz.utc.localize(naive_date)
            self.articles.append(details)



class TSNScraper(Scraper):
    """
    Rip articles from TSN.ca
    """
    def scrape_all(self):
        """
        Traverse the page content and extract the key information about each
        article. That being: The article headline and the URL to the actual
        article.
        """
        self.articles = []
        request = requests.get(self.url)
        page = BeautifulSoup(request.text, "html.parser")
        unfiltered_articles = page("article")
        articles = [
            x for x in unfiltered_articles if
            "normal" not in x["class"] and
            "three-column" not in x["class"]
        ]

        for article in articles:
            details = {}
            details["pub_date"] = None
            generic_classes = ("promo-image-related"
                               , "promo-image"
                               , "promo-no-image-related"
                              )

            # configure our DOM search terms
            if "super-promo" in article["class"]: #the big article up top
                header_size = "h2"
                headline_class = "headline-super"

            elif set(generic_classes).isdisjoint(set((article["class"]))):
                header_size = "h3"
                headline_class = "headline"
                print("Generic article... we should probably skip it")
                continue


            try:
                details["article_title"] = article.find(header_size).text
            except AttributeError as exception:
                print(
                    "Error retrieving article title. Exception: {}".format(
                        exception
                    )
                )
                details["article_title"] = "TSN Article"

            try:
                article_rel = article.find(
                    class_=headline_class
                ).find("a")["href"]
                details["article_url"] = urljoin(self.url, article_rel)
            except AttributeError as exception:
                print("Couldn't get url for [{}]".format(
                    details["article_title"]))
            if "article_title" in details.keys() and \
               "article_url" in details.keys():
                self.articles.append(details)



        # TSN displays a row of three stories which we may or may not care
        # about...  We need different logic to extract their details.
        # extra_stories = page(class_="three-column")

class SportsnetScraper(Scraper):
    """
    Scrapes sportsnet.ca by topic
    """

    def scrape_all(self):
        """
        Traverse the page at the feed url and get headlines and article URLs.
        :return:
        """

        headlines = self.content.select(
            ".headlines.module > ul > li > a"
        )
        for headline in headlines:
            article = {}
            article["article_title"] = headline.text.strip()
            article["article_url"] = headline["href"]
            article["pub_date"] = None
            self.articles.append(article)
