from newsapi import NewsApiClient
from newsplease import NewsPlease

class newsapi():
    def __init__(self,query):
        self.query=query

    def geturls(self):
        newsapi = NewsApiClient(api_key='63fb615d56a749ef8837fbf084c88a3c')
        all_articles = newsapi.get_everything(q=self.query,
                                          language='en',
                                          sort_by='relevancy',
                                          page=1
                                          )
        urls=[]
        for i in range(3):
            urls.append(all_articles["articles"][i]["url"])
        return urls

    def getcontent(self):
        articles=[]
        urls5=self.geturls()
        for i in urls5:
            article = NewsPlease.from_url(i)
            articles.append(article)
        return articles
"""
x=newsapi("nirav modi arrested")

print(x.geturls())
x.getcontent()"""
