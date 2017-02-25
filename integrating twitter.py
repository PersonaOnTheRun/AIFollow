#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:45:32 2017

@author: cammilligan
"""

#E1F95CC0F1

#witter:site value @WashingtonPost
#keywords content


from bs4 import BeautifulSoup
import requests

url= 'https://www.flipkart.com'
page3= requests.get("https://www.washingtonpost.com/news/post-nation/wp/2017/02/14/its-like-the-rock-was-melting-the-stunning-destruction-at-oroville-dam-and-the-work-ahead/?utm_term=.956d2f17db67")
soup3= BeautifulSoup(page3.text)


keywords = []
twitterhandle = []

try:
    desc= soup3.find(attrs={'name':'keywords'})
    keywords.append(desc['content']) 
except:
    if len(keywords) == 0:
        desc= soup3.find(attrs={'name':'Keywords'})
        keywords.append(desc['content'])
    else:
        print("no keywords")    


try:
    desc2 = soup3.find(attrs={'name':'twitter:site'})
    twitterhandle.append(desc2['value'])
except:
    print("no twitter") 
    
    


print(keywords)
print(twitterhandle)
