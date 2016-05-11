# coms3101

Program Architecture
Main.py -> Covers all functionality, contains a robust test data set to prevent having to constantly call to csv’s during testing 
Txt & Csv files -> the result of manually downloaded or webscrapped data that is used within our visualization

Methods in Main.py

make_dates(months(int), month_dict(dictionary)) 
Returns an array of string dates in the format  ‘0101’ , ‘0202’ etc. We referred to dates this way throughout our script because these dates could be directly inserted into the web url. Had we had more time we would like to have created a more robust structure of dealing with dates

get_headlines()
Returns a dictionary in the format {‘date’:[list of headlines]…} from our webscrapped data. We webscrapped the Reuters list of daily headlines using Beautiful Soup, found the html class in which the headline title was stored, and removed the text.


