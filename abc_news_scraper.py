# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:45:32 2021

@author: Abena Laast
"""
#web scraping tutorial
#https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558

#downloading packages in spyder tutorial
#https://www.miamioh.edu/cads/students/student-resources/python/beginners/downloading-installing-packages/

# importing the necessary packages
import requests
from bs4 import BeautifulSoup

news_urls = ["https://abcnews.go.com/Health/Coronavirus", "https://www.cnn.com/search?q=covid&size=10&type=article"]
#url of the coronavirus stories section of abc
URL = news_urls[0]
r1 = requests.get(URL)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html.parser')
#https://realpython.com/beautiful-soup-web-scraper-python/

#class with all top covid articles
results = soup1.find(class_='ContentList')
# def getHTML() :
#     return(results.prettify())
'''
#class with an individual article
article = results.find(class_='ContentList__Item')
#class with an individual article's url
article_url = results.find(class_='AnchorLink News__Item external flex flex-row')
#class with an individual article's title
article_title = results.find(class_='News__Item__Headline')
'''
#all article titles
articles = results.find_all(class_='News__Item__Headline')
#all urls
urls = results.find_all(class_='AnchorLink News__Item external flex flex-row')
'''
#prints html with the results
print(results.prettify())
print("\n\n")

#prints html with first article
print(article.prettify())

#prints the url of the first article
print(article_url['href'])

#prints title of first article
print(article_title['aria-label'])
'''
#prints all top covid stories and their urls
names = []
links = []

for x in range(len(articles)):
    names.append(articles[x]['aria-label']+"\n")
    links.append(urls[x]['href']+"\n")

print(names)

#return names & urls to display
def get_names():
    return names
def get_URLS():
    return links

