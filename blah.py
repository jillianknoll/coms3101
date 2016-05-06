from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#import matplotlib.pyplot
#import numpy as np
#import matplotlib.pyplot as plt

def get_results():
    rows = []
    month_dict = {1:31, 2:29, 3:31, 4:30}
    months_test = {1:4, 2:5}
    search_url = 'http://www.reuters.com/resources/archive/us/20160123.html'
    search_base = 'http://www.reuters.com/resources/archive/us/20160'
    search_end = ".html"
    lis = []
    for i in range(1,2):
        day  = i + 1
        if day < 10:
            day = '01'
        else:
            day - str(day)
        print(search_base + str(i) + day + search_end)
        soup = BeautifulSoup(urlopen(search_base + str(i) + day + search_end).read(), 'html.parser')
        print("Date" + str(i))
        totalcount = soup.find_all('div', {'class':'module'})
        for row in totalcount:
            #remove the html tags
            tokens = str(row).split('>')
            for item in tokens:
                #if it starts with a letter then its text
                #otherwise unwanted data
                if item[0:1].isalpha():
                    #remove ending html tag portion that wasn't removed by split()
                    #text is located at first index
                    lis.append(item.split('<')[0])
    for l in lis:
        print(l)


   # soup = BeautifulSoup(urlopen(search_url).read(), 'html.parser')
   # totalcount = soup.find_all('div', {'class':'module'})
   # for a in totalcount:
    #    x = str(a).split('>')
     #   for y in x:
      #      if y[0:1].isalpha():
       #         z = y.split('<')
        #        print(z[0])


if __name__ == "__main__":
    get_results()