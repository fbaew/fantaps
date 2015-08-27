class Scraper():

    def __init__(self, url):
        self.feed_url = url



def main():
    url_config = open("urls","r")
    for line in url_config:
        scraper = Scraper(line)
        scraper.get_latest_items()
 
