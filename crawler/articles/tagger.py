from articles.models import Article

class Tagger():
    keywords = []
    def __init__(self):
        pass
    
    def get_tag_scores(self,article):
        text = article.article_text
        '''
        Count the keyword bucket occurences, and return the most frequent one.
        '''
        scores = {}
        max_mentions = 0
        best_keyword = ""
        for category in self.keywords:
            scores[category[0]] = 0;
            for keyword in category:
                scores[category[0]] += text.upper().count(
                    keyword.upper()
                )
                if scores[category[0]] > max_mentions:
                    max_mentions = scores[category[0]]
                    best_keyword = category[0]
        print("[{}] - {}".format(text,best_keyword))
        print(scores)
        print(sorted(scores,key=scores.get))
        return {
            "scores":scores,
            "likeliest_tag":best_keyword,
        }

    
class TeamTagger(Tagger):
    def __init__(self):
        pass

class CityTagger(Tagger):
    def __init__(self):
        super(CityTagger,self).__init__()
        self.keywords = [
            ("Anaheim", "Ducks"),
            ("Arizona","Coyotes"),
            ("Boston", "Bruins"),
            ("Buffalo","Sabres"),
            ("Calgary","Flames"),
            ("Carolina","Hurricanes"),
            ("Chicago","Blackhawks"),
            ("Colorado","Avalanche"),
            ("Columbus","Blue Jackets"),
            ("Dallas","Stars"),
            ("Detroit","Red Wings"),
            ("Edmonton","Oilers"),
            ("Florida","Panthers"),
            ("Los Angeles","Kings"),
            ("Minnesota","Wild"),
            ("Montreal","Canadiens"),
            ("Nashville","Predators"),
            ("New Jersey","Devils"),
            ("New York","Islanders"),
            ("New York","Rangers"),
            ("Philadelphia","Flyers"),
            ("Pittsburgh","Penguins"),
            ("Ottawa","Senators"),
            ("San Jose","Sharks"),
            ("St Louis","Blues"),
            ("Tampa Bay","Lightning"),
            ("Toronto","Maple Leafs"),
            ("Vancouver","Canucks"),
            ("Washington","Capitals"),
            ("Winnipeg","Jets"),
        ]
        
class SportTagger(Tagger):
    def __init__(self):
        super(SportTagger,self).__init__()
        self.keywords = [
            ("Hockey","NHL","N.H.L."),
            ("Baseball"
                ,"MLB","M.L.B."
                ,"World Series"
                ,"Orioles"
                ,"Red Sox"
                ,"White Sox"
                ,"Indians"
                ,"Tigers"
                ,"Astros"
                ,"Diamondbacks"
                ,"Braves"
                ,"Cubs"
                ,"Reds"
                ,"Rockies"
                ,"Dodgers"
                ,"Royals"
                ,"Marlins"
                ,"Angels"
                ,"Twins"
                ,"Yankees"
                ,"Athletics"
                ,"Mariners"
                ,"Rays"
                ,"Rangers"
                ,"Brewers"
                ,"Mets"
                ,"Phillies"
                ,"Pirates"
                ,"Padres"
                ,"Giants"
                ,"Cardinals"
                ,"Blue Jays"
                ,"Nationals"),
            ("Golf","PGA","P.G.A."),
            ("Basketball","NBA","N.B.A."),
            ("Football","NFL","N.F.L.","CFL","C.F.L.")
        ]
