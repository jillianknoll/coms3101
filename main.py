from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import unittest as unit
import csv
import subprocess
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
global month_dict
import pdb
month_dict = {1:31, 2:29, 3:31, 4:30, 5:5}
global months
months = {1:"January 2016", 2:"February 2016", 3:"March 2016", 4:"April 2016"}

class InputZeroException(Exception):
    pass

class InvalidInputException(Exception):
    pass

class FileNotFoundException(Exception):
    pass

class NonDictionaryInputException(Exception):
    pass

class FileOverwriteException(Exception):
    pass


def test_dict():
    """contains small test dataset for testing"""
    di = {'0102': ['Raptors get win as Hornets scoring dries up in final minutes', 'Buffalo Bills - PlayerWatch', 'Bulls win laugher vs. Knicks', 'Florida coach Gallant gets contract extension', 'Raptors take control late to beat Hornets', 'McCaffrey sets Rose Bowl records in Stanford rout', "UPDATE 1-Bill Cosby's wife must testify in civil case against him, judge rules", 'Heat look on the Whiteside in 106-82 win', 'NIMBLE STORAGE SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: Kahn Swick &amp; Foti, LLC Reminds Investors With Losses in Excess of $100,000 of Lead Plaintiff Deadline in Class Action Lawsuit Against Nimble Storage, Inc', 'Laos, Hmong Community, Veterans Reflect Upon Efforts in Washington, U.S. Congress'], '0104': ['Asian bankers will shift from deals to distress', 'Seahawks shut down Cardinals', 'Top 25 roundup: Cal hands Utah 2nd loss in row', 'Manning returns to help Broncos earn AFC top seed', 'BRIEF-Shenzhen Worldunion Properties Consultancy terminates acquisition plan', 'Operation to flush out Indian air base attackers enters second night', 'BRIEF-Jiangsu JiuJiuJiu Technology unit to recall syrup', "Indonesia's tourist arrivals rise 1.70 pct y/y in Nov", 'BRIEF-Nanfang Black Sesame to acquire edible oil firm for 625 mln yuan', 'Colorado 56, Stanford 55'], '0302': ['Indiana edges Iowa to seal outright Big Ten title', 'CORRECTED-HKEx 2015 profit surges 54 pct to record high as trading volumes rise', 'Australia softens sanctions against Iran', 'Chinese overseas investment tops $1 trillion over a decade - report', 'Chongqing blazes economic trail as Bo scandal recedes', 'LME revenue from trading fees, tariffs surges 51 pct in 2015', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'Parts of Great Barrier Reef face permanent destruction due to El Nino - scientists', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'BRIEF-United Bank For Africa appoints Kennedy Uzoka as group MD/CEO'], '0204': ['ViaCyte Acquires Rights to BetaLogics Assets, Expanding and Extending Industry-Leading Portfolio for Stem Cell-Derived Approaches to Type 1 Diabetes', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'No. 7 Kansas overcomes slow start, beats Kansas State', 'China, HK stocks rebound as dollar tumble ease yuan depreciation fears', 'Indonesia 2016 rubber exports seen declining at least 8 pct -industry assoc', 'Hornets beat LeBron for first time since 2010', 'Whiteside returns to help Heat defeat Mavericks', 'U.S. House panel subpoenas hacked federal agency for documents', 'MIDEAST STOCKS - Factors to watch - Feb 4'], '0202': ["BRIEF-Indonesia's XL Axiata eyes funds from rights offer, tower sale", 'UPDATE 3-Bernie Sanders shows strong momentum on social media', 'Lawyers from Keller Rohrback Share Nobel Peace Prize Nomination', "Malaysia's central bank to launch new Islamic T-bills this week", 'BRIEF-Tiger Branded Consumer Goods Q1 loss before tax 975.3 mln naira', 'Oilers hope returning McDavid can stop them slipping further', 'BRIEF-Henan Kedi Dairy Industry to issue shares as 2015 dividend', "Broncos' Manning says no decision yet on retirement", 'BRIEF-Yunnan Hongxiang Yixintang Pharma sells stake in Kunming-based pharma co', 'BRIEF-Yunnan Hongxiang Yixintang Pharma buys Zhengzhou-based co'], '0205': ['Toews nets OT winner for Blackhawks', 'Rockets finsih strong in win vs. Suns', 'USC 80, UCLA 61', "BRIEF-Vietnam's Military Bank says 2015 net profit up 0.8 pct y/y", 'Oil falls 2 pct as producer meet uncertainty offsets weak dollar', 'Indian lenders, central bank, square off over cash shortages', 'China money rates steady ahead of Lunar New Year festival on c.bank injections', 'Eberle leads Oilers in rout of Senators', 'Mosquito repellant sales boom in Brazil amid Zika scare', "Doubting India's 'fastest-growing' GDP stats, economists devise their own"], '0103': ['Davis paces Pelicans past Mavericks', 'San Diego State 70, Utah State 67', 'Spurs ground Rockets to stay unbeaten in San Antonio', 'Bucks 95, Timberwolves 85', 'MIDEAST STOCKS - Factors to watch - Jan 3', 'Stream TV Networks to Exhibit at CES Unveiled Las Vegas 2016, Booth 13633', 'New Mexico 77, Fresno State 62', 'George carries Pacers past Pistons', 'Cavaliers defeat Magic for 13th straight time', "Blue Jackets' rookie goalie stops Capitals in shootout"], '0301': ['Venture+ Forum at HIMSS16 Annual Conference Announces Four Companies Advancing to Final Pitch Competition', 'Datsyuk lifts Red Wings past Stars in OT', 'Mexico says 11 pregnant women infected with Zika', 'Schenn hat trick helps Flyers defeat Flames', 'CORRECTED-Taiwan stocks up tracking overseas markets; main index at 3-mth high', "Fitch Affirms Finnet Indonesia at 'A(idn)'; Stable Outlook", "Olympics-Gatlin's coach steps down as U.S. relay boss for Rio", "Indonesia's foreign tourist arrivals rise 2.2 pct y/y in Jan", "Brazil's Petrobras corruption investigation targets Lula", 'China court jails 24 over $1.5-bln financial fraud - Xinhua'], '0201': ['MOVES-Credit Suisse hires Stoehr in new Asia-Pacific financing role', 'TABLE-India cenbank says reverse repo bids rise to 116.15 bln rupees', "BRIEF-Oceanwide terminates plan to sell unit's stakes to Minsheng Holdings", 'Law enforcement bikers fought outlaw gang in deadly Denver melee', 'Brokerage firm RCS Capital files for bankruptcy', "Indonesia's tourist arrivals drop 0.16 pct y/y in Dec", 'BRIEF-Shanghai New World gets regulatory approval to issue shares in private placement', 'A hefty earnings week ahead', 'No. 23 Oregon completes sweep in Arizona', 'Dubai Investments Q4 net profit rises 2.6 pct'], '0101': ['Dr. Paula Watkins: First African-American Virtual School Founder', "Doan breaks Coyotes' record in win vs. Jets", "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Stars rout Predators to end year in style', 'Puerto Rico reports first case of Zika virus, spread by mosquitoes', "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", "UPDATE 2-Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Clippers cap trip with win over Pelicans', 'Morpx Inc to Exhibit at 2016 International CES, Sands, Hall G - 80851', 'Germany says it has information Islamic State planned suicide attacks in Munich'], '0203': ["Qatar's Gulf International Services swings to Q4 net loss", 'Crawford carries Blackhawks past Avalanche', 'UPDATE 1-China 2015 gold output dips 0.4 pct, consumption rises', 'Brown scores twice as Kings defeat Coyotes', "Lenovo's Q3 revenue falls 8 pct to $12.9 bln; net profit beats estimates", 'Get answers to all your burning college football recruiting questions at C Spire - SuperTalk Mississippi 2016 National Signing Day event on Feb. 3', 'KFC wins China payout over mutant chicken rumors', 'SE Asia Stocks-Weak; Thai index off lows ahead of cenbank rate decision', 'DePaul takes down No. 11 Providence', 'DLF Q3 net profit up 24 percent as rental income rises'], '0303': ['China stocks firm, bolstered by property sector; Hong Kong shares dip', 'Alibaba finance arm in talks to invest in Chinese media group Caixin -sources', 'Call for government unity as Australian PM faces critical budget, election', 'UPDATE 1-Vatican cardinal denies attempts to cover up child sex abuse', 'Donald Trump Jr. appears alongside white supremacist in radio show', "FOREX-Dollar gains with Friday's US jobs data in focus", 'The Scientology Information Center Answers “What is Scientology” During Clearwater’s Blast Friday', 'Spurs run away from Detroit in win', 'Asia to see first gasoline squeeze in more than 15 years', 'Maruti Suzuki to hike car prices after new green tax']}
    return di

def make_dates(months, month_dict):
    """takes argument months and returns an array of string dates from Jan 1 2016 in the form '0101', '0102', '0103' etc"""
    #global dates
    if months == 0:
        raise InputZeroException("Must have nonzero argument")
       # raise Exception("Must have nonzero input")
    if not (type(months) == int):
        raise InvalidInputException("Must have integer input")
    month_dic = month_dict
   # dates = ['0101', '0102', '0202']
    #return list of dates to map to other variables
    #return in the form "0101", "0102" corresponding to Jan. 1, Jan. 2...
   # month_dict = {1:31, 2:29, 3:31, 4:30}
    d_list = []
    for i in range(1,months+1):
        if i < 10:
            m = '0' + str(i)
        else:
            m = str(i)
        d = month_dic[i]
        for l in range(1,d+1):
            if l < 10:
                date = '0' + str(l)
                d_list.append(m + date)
            else:
                date = str(l)
                d_list.append(m + date)
               # print("hey")
   # print("breakpt")
    return d_list
  #  return dates



def get_headlines():
    """returns a dictionary containing the headlines"""
    rows = []
  #  month_dict = {1:31, 2:29, 3:31, 4:30}
  #  months_test = {1:4, 2:5}
    search_url = 'http://www.reuters.com/resources/archive/us/20160123.html'
    search_base = 'http://www.reuters.com/resources/archive/us/2016'
    search_end = ".html"
    dates = make_dates(4,month_dict ) #now can use the global dates variable
    for i in dates:
        print(i)
    date_headline = {}
    for i in dates:
        daily_headlines = []
        #print(search_base + str(i) + day + search_end)
        soup = BeautifulSoup(urlopen(search_base + i + search_end).read(), 'html.parser')
       # print("Date" + str(i))
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
                    daily_headlines.append(item.split('<')[0])
        #trunc_list = daily_headlines[0:10] # for testing
        #date_headline[i] = trunc_list
        date_headline[i] = daily_headlines
    return date_headline
#    return dates

def write_csv():
    """writes headline dictionary to a csv in the format ['date','headline']"""
    if os.path.isfile("headlines.csv"):
        raise FileOverwriteException
    headlines= get_headlines()
    #throw exception if trying to overwrite file
        #don't want to overwrite webscraped file
    with open('headlines.csv', 'w') as file:
        writer = csv.writer(file)
        for y in headlines.keys():
            currlist = headlines[y]
            for num in range(len(currlist)):
                writer.writerow((y, currlist[num]))

def parse_lang_dict():
    """parses the postive-words and negative words dictionaries"""
    if not os.path.isfile("negative-words.txt"):
        raise FileNotFoundException
    if not os.path.isfile("positive-words.txt"):
        raise FileNotFoundException
    with open('negative-words.txt','r') as f:
        neg_lines = []
        for line in f:
            strip_nl = line.rstrip()
            neg_lines.append(strip_nl)
    with open('positive-words.txt','r') as f:
        pos_lines = []
        for line in f:
            strip_nl = line.rstrip()
            pos_lines.append(strip_nl)
    return neg_lines, pos_lines

def parse_dow_csv():
    dow_dict = {}
    """parses the csv for the closing prices of the DOW"""
    with open('DJIA.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if str(row[1])[0:1].isdigit():
                curr_date = str(row[0])[5:7] + str(row[0])[8:10]
                dow_dict[curr_date] = float(row[1].rstrip())
    return dow_dict


def make_tokens(testdict):
    """makes tokens from the list of headlines"""
   # print("tokens")
    if type(testdict) is not type({'a':1}):
        raise NonDictionaryInputException
    test_list = testdict
    #test_list = get_headlines()
    tokened_words_to_dates = {}
    date_list = testdict.keys()
    for i in date_list:
        tokened = []
        curr_list = test_list[i]
        for headline in curr_list:
            word_list = headline.split(' ')
            for word in word_list:
                word = re.sub(r'\W+', '', word.lower())
                if word.isalpha():
                    tokened.append(word)
        tokened_words_to_dates[i] = tokened
    return tokened_words_to_dates


def calc_sentiment(testdict):
    """calculates the sentiment as a quantity"""
    if type(testdict) is not type({'a':1}):
        raise NonDictionaryInputException
    tokens = make_tokens(testdict)
    #print(tokens)
    date_to_positive = {}
    date_to_negative = {}
    date_to_ratio = {}
    words = parse_lang_dict()
    positive_words = words[1]
    negative_words = words[0]
    date_list = testdict.keys()
    date_list = list(date_list)
    #print(date_list)
    for date in date_list:
        positive_count = 0
        negative_count = 0
        words = tokens[date]
        for word in words:
            if word in positive_words:
                positive_count = positive_count + 1
            elif word in negative_words:
                negative_count = negative_count + 1
        date_to_positive[date] = positive_count
        date_to_negative[date] = negative_count
    #calculate sentiment ratios 
    #using sentiment = (positive - negative)/(positive + negative)
    for date in date_list:
        if date_to_positive[date] + date_to_negative[date] == 0:
            #store 0
            date_to_ratio[date] = 0
        else:
            date_to_ratio[date] = (date_to_positive[date] - date_to_negative[date]) / (date_to_positive[date] + date_to_negative[date])
    return date_to_ratio
  #  print(date + " Positive: " + str( date_to_positive[date]) + " Negative: " + str(date_to_negative[date]))

def parse_sentiment_csv():
    if not os.path.isfile("headlines.csv"):
        raise FileNotFoundException
    headlines_dict = {}
    temp_list = []
    curr_date = ''
    prev_date = ''
    with open('headlines.csv','r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[0] not in headlines_dict:
                headlines_dict[line[0]] = []
            headlines_dict[line[0]].append(line[1])

    for key in headlines_dict:
        curr_list = headlines_dict[key]
        curr_list = curr_list[0:30]
        headlines_dict[key] = curr_list
    return headlines_dict
  #  print(headlines_dict.keys())
#

def make_graphs():
    """outputs the graphs of 1) total returns"""
    #finds the number of days each month that the positive sentiment predicts positive returns
    #number of days that a positive sentiment predicts market rise
    #return to date from the strategy over 4 months 
    global months
    dow_dict = parse_dow_csv()
    a = list(dow_dict.keys())
    a = sorted(a)
    returns = {}
    for i in range(1,len(a)):
        returns[a[i]] = (dow_dict[a[i]] - dow_dict[a[i-1]])

    #returns to date from buying the day after positive sentiment and selling the day after negative sentiment
    return_to_month_pos = {1:0, 2:0, 3:0, 4:0}
    return_to_month_neg = {1:0, 2:0, 3:0, 4:0}
    sentiments = calc_sentiment(parse_sentiment_csv())
    for num in range(0,len(a)-1):
        if returns[a[num + 1]] > 0 and sentiments[a[num]] > 0:
            date_month = int(a[num+1][0:2])
            new_win_count = return_to_month_pos[date_month] + 1
            return_to_month_pos[date_month] = new_win_count
        elif returns[a[num + 1]] < 0 and sentiments[a[num]] < 0:
            date_month = int(a[num+1][0:2])
            new_win_count = return_to_month_neg[date_month] + 1
            return_to_month_neg[date_month] = new_win_count
    print(return_to_month_pos)
    print(return_to_month_pos.keys())
    print(return_to_month_pos.values())


    N = 4
    pos_values = list(return_to_month_pos.values())

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, pos_values, width, color='r')
    neg_values = list(return_to_month_neg.values())
    rects2 = ax.bar(ind + width, neg_values, width, color='y')

    ax.set_ylabel('Number of Days Per Month')
    ax.set_title("Number of Days +/- Sentiment Predicted Corresponding Market Movement")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(list(months.values()))

    ax.legend((rects1[0], rects2[0]), ('Positive Sentiment', 'Negative Sentiment'))

    plt.show()


    
    #graph the number of correctly predicted positive and negative returns from every month 




if __name__ == "__main__":
    #print usage statement
    if(len(sys.argv) > 1 and sys.argv[1]== 'help'):
        print("usage: python main.py OR python run_tests")
    #run tests
    if(len(sys.argv) > 1 and sys.argv[1] == 'run_tests'):
        subprocess.call(" python tests.py", shell=True)
    if(len(sys.argv) > 1 and sys.argv[1] == 'debug'):
        pdb.run(make_graphs())
    if(len(sys.argv) > 1 and sys.argv[1] == 'make_graphs'):
        make_graphs()

    make_tokens('a')

