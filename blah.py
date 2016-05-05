from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

def get_results():
    """will return a tuple of (lists, boroughs) where lists is a list of 5 lists corresponding to the couch prices in each borough and boroughs is the list of boroughs in the same order"""
    rows = []
    #get the first page for all five boroughs
    search_url = ['https://newyork.craigslist.org/search/brk/fua', 'https://newyork.craigslist.org/search/stn/fua', 'https://newyork.craigslist.org/search/mnh/fua', 'https://newyork.craigslist.org/search/brx/fua', 'https://newyork.craigslist.org/search/que/fua']
    couch = '?query=couch'
    couch_next = '?s=100&query=couch'

    url_dict = {'https://newyork.craigslist.org/search/brk/fua':'brooklyn','https://newyork.craigslist.org/search/stn/fua':'staten island', 'https://newyork.craigslist.org/search/mnh/fua':'manhattan', 'https://newyork.craigslist.org/search/brx/fua':'bronx', 'https://newyork.craigslist.org/search/que/fua':'queens'}
    soup = [ BeautifulSoup(urlopen(s + couch).read(), 'html.parser') for s in search_url]

    #extract the total count for each neighborhood
    totalcount = [soup_el.find_all('span', {'class':'totalcount'}) for soup_el in soup]
    neighborhood_totals = []

    #count the totals for each neighborhood
    for t in totalcount:
        neighborhood_totals.append(int(re.findall('\d+', str(t[0::2]))[0]))

    #extract price rows from soup object
    rows = [soup_el.find_all('span', {'class': 'price'}) for soup_el in soup]


    #if the count > 100, request data from a new page
    for n in range(len(search_url)):
        #print(str(n) + url_dict[search_url[n]])
        #print(neighborhood_totals[n])
        if neighborhood_totals[n] > 100:
            new_url = search_url[n] + couch_next
            #print('Hi')
            new_soup = BeautifulSoup(urlopen(new_url).read(), 'html.parser')
            new_rows = new_soup.find_all('span', {'class': 'price'})
            rows[n] = rows[n] + new_rows

    #extract the integer from each row and replace in list
    new_rows = []
    temp_row = []

    for row in rows: # a list of lists --> nested for loops
        temp_row = []
        for r in row[0::2]:
            temp_row.append(int(re.findall('\d+', str(r))[0])) # find_all returns list need first index
           # print(r)
        new_rows.append(temp_row)

    #map row names to the search url to identify borough
    row_map = [url_dict[search_url[n[0]]] for n in enumerate(search_url)]
    return new_rows, row_map