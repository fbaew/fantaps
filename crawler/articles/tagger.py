class Tagger():
    keywords = []
    def __init__(self):
        pass
    
    def get_tag_scores(self,text):
        scores = {}
        max_mentions = 0
        best_keyword = ""
        for category in self.keywords:
            scores[category[0]] = 0;
            for keyword in category:
                scores[category[0]] += text.count(keyword)
                if scores[category[0]] > max_mentions:
                    max_mentions = scores[category[0]]
                    best_keyword = category[0]
        return {
            "scores":scores,
            "likeliest_tag":best_keyword,
        }

    
class TeamTagger(Tagger):
    def __init__(self):
        pass

class SportTagger(Tagger):
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