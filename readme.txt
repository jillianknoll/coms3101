# coms3101

Program Architecture
Main.py -> Covers all functionality, contains a robust test data set to prevent having to constantly call to csv’s during testing 
Txt & Csv files -> the result of manually downloaded or webscrapped data that is used within our visualization

make_dates(months(int), month_dict(dictionary)) 
Returns an array of string dates in the format  ‘0101’ , ‘0102’ etc referring to Jan 1, Jan 2... Since we started our web scraping for Jan 1, 2016 we did not include years in the date format. We referred to dates this way throughout our script because these dates could be directly inserted into the web url. Had we had more time we would like to have created a more robust structure of dealing with dates

get_headlines()
Returns a dictionary in the format {‘date’:[list of headlines]…} from our webscrapped data. We web scraped the Reuters list of daily headlines using Beautiful Soup, found the html class in which the headline title was stored, and removed the text.

write_csv()
Is designed to write the webs scraped headlines to a csv file titled ‘test.csv’ in the format [‘date’,’headline’]

parse_lang_dict()
Is designed to parse the text files “negative-words.txt” and “positive-words.txt” that were taken from this University of Illinois researcher (https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html).
The contents of both text files are stored in a dictionary that is returned.

parse_dow_csv()
Is designed to parse the csv storing the DJIA closing values in integers alongside their date in the document wide date format of ‘0101’, ‘0102’… in a dictionary that is returned.

make_tokens(testdict)
Make tokens turns the list of headlines per day into a list of words per day. Any non-alpha characters are removed and the words in a given date are stored in a list as that date’s value in a dictionary. The dictionary is returned.

calc_sentiment(testdict)
This function calls the make_tokens function on the testdict (dictionary) argument. The function iterates through every word in a date’s word list and counts the number of words that are associated with the previously parsed word lists. After the positive and negative words are counted, the function calculates the sentiment ratio as described here (http://www.cloudera.com/documentation/other/tutorial/CDH5/Hadoop-Tutorial/ht_example_4_sentiment_analysis.html) wherein sentiment_ratio = (count_positive_words – count_negative_words) / (count_positive_words – count_negative_words). The sentiment ratio is stored as a dictionary value corresponding to dates as keys.

parse_sentiment_csv()
Reads the ‘headline.csv’ file that was created in the write_csv() function to store the headlines as lists. The headline lists are taken as values for dictionary keys corresponding to the date. The dictionary is returned.

make_graphs()
This function calculates the returns between Dt and Dt-1¬, corresponding to the change in closing price between today and yesterday for the DJIA. The values corresponding to the change in closing price are stored as values in a dictionary with dates as keys.

To find the values shown on the graph “Number of Days +/- Sentiment Predicted Corresponding Market Movement” we calculated the number of days per month where there was both a 1) positive trend in the DJIA and 2) a positive sentiment ratio the day before. We also calculated the same for negative ratios combined with a daily negative outcome of the DJIA. These values were stored in dictionaries. We then created a bar graph of the 




















