from bs4 import BeautifulSoup
from urllib.request import urlopen
#import matplotlib.pyplot
#import numpy as np
#import matplotlib.pyplot as plt

def test_dict():
    di = {'0102': ['Raptors get win as Hornets scoring dries up in final minutes', 'Buffalo Bills - PlayerWatch', 'Bulls win laugher vs. Knicks', 'Florida coach Gallant gets contract extension', 'Raptors take control late to beat Hornets', 'McCaffrey sets Rose Bowl records in Stanford rout', "UPDATE 1-Bill Cosby's wife must testify in civil case against him, judge rules", 'Heat look on the Whiteside in 106-82 win', 'NIMBLE STORAGE SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: Kahn Swick &amp; Foti, LLC Reminds Investors With Losses in Excess of $100,000 of Lead Plaintiff Deadline in Class Action Lawsuit Against Nimble Storage, Inc', 'Laos, Hmong Community, Veterans Reflect Upon Efforts in Washington, U.S. Congress'], '0104': ['Asian bankers will shift from deals to distress', 'Seahawks shut down Cardinals', 'Top 25 roundup: Cal hands Utah 2nd loss in row', 'Manning returns to help Broncos earn AFC top seed', 'BRIEF-Shenzhen Worldunion Properties Consultancy terminates acquisition plan', 'Operation to flush out Indian air base attackers enters second night', 'BRIEF-Jiangsu JiuJiuJiu Technology unit to recall syrup', "Indonesia's tourist arrivals rise 1.70 pct y/y in Nov", 'BRIEF-Nanfang Black Sesame to acquire edible oil firm for 625 mln yuan', 'Colorado 56, Stanford 55'], '0302': ['Indiana edges Iowa to seal outright Big Ten title', 'CORRECTED-HKEx 2015 profit surges 54 pct to record high as trading volumes rise', 'Australia softens sanctions against Iran', 'Chinese overseas investment tops $1 trillion over a decade - report', 'Chongqing blazes economic trail as Bo scandal recedes', 'LME revenue from trading fees, tariffs surges 51 pct in 2015', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'Parts of Great Barrier Reef face permanent destruction due to El Nino - scientists', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'BRIEF-United Bank For Africa appoints Kennedy Uzoka as group MD/CEO'], '0204': ['ViaCyte Acquires Rights to BetaLogics Assets, Expanding and Extending Industry-Leading Portfolio for Stem Cell-Derived Approaches to Type 1 Diabetes', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'No. 7 Kansas overcomes slow start, beats Kansas State', 'China, HK stocks rebound as dollar tumble ease yuan depreciation fears', 'Indonesia 2016 rubber exports seen declining at least 8 pct -industry assoc', 'Hornets beat LeBron for first time since 2010', 'Whiteside returns to help Heat defeat Mavericks', 'U.S. House panel subpoenas hacked federal agency for documents', 'MIDEAST STOCKS - Factors to watch - Feb 4'], '0202': ["BRIEF-Indonesia's XL Axiata eyes funds from rights offer, tower sale", 'UPDATE 3-Bernie Sanders shows strong momentum on social media', 'Lawyers from Keller Rohrback Share Nobel Peace Prize Nomination', "Malaysia's central bank to launch new Islamic T-bills this week", 'BRIEF-Tiger Branded Consumer Goods Q1 loss before tax 975.3 mln naira', 'Oilers hope returning McDavid can stop them slipping further', 'BRIEF-Henan Kedi Dairy Industry to issue shares as 2015 dividend', "Broncos' Manning says no decision yet on retirement", 'BRIEF-Yunnan Hongxiang Yixintang Pharma sells stake in Kunming-based pharma co', 'BRIEF-Yunnan Hongxiang Yixintang Pharma buys Zhengzhou-based co'], '0205': ['Toews nets OT winner for Blackhawks', 'Rockets finsih strong in win vs. Suns', 'USC 80, UCLA 61', "BRIEF-Vietnam's Military Bank says 2015 net profit up 0.8 pct y/y", 'Oil falls 2 pct as producer meet uncertainty offsets weak dollar', 'Indian lenders, central bank, square off over cash shortages', 'China money rates steady ahead of Lunar New Year festival on c.bank injections', 'Eberle leads Oilers in rout of Senators', 'Mosquito repellant sales boom in Brazil amid Zika scare', "Doubting India's 'fastest-growing' GDP stats, economists devise their own"], '0103': ['Davis paces Pelicans past Mavericks', 'San Diego State 70, Utah State 67', 'Spurs ground Rockets to stay unbeaten in San Antonio', 'Bucks 95, Timberwolves 85', 'MIDEAST STOCKS - Factors to watch - Jan 3', 'Stream TV Networks to Exhibit at CES Unveiled Las Vegas 2016, Booth 13633', 'New Mexico 77, Fresno State 62', 'George carries Pacers past Pistons', 'Cavaliers defeat Magic for 13th straight time', "Blue Jackets' rookie goalie stops Capitals in shootout"], '0301': ['Venture+ Forum at HIMSS16 Annual Conference Announces Four Companies Advancing to Final Pitch Competition', 'Datsyuk lifts Red Wings past Stars in OT', 'Mexico says 11 pregnant women infected with Zika', 'Schenn hat trick helps Flyers defeat Flames', 'CORRECTED-Taiwan stocks up tracking overseas markets; main index at 3-mth high', "Fitch Affirms Finnet Indonesia at 'A(idn)'; Stable Outlook", "Olympics-Gatlin's coach steps down as U.S. relay boss for Rio", "Indonesia's foreign tourist arrivals rise 2.2 pct y/y in Jan", "Brazil's Petrobras corruption investigation targets Lula", 'China court jails 24 over $1.5-bln financial fraud - Xinhua'], '0201': ['MOVES-Credit Suisse hires Stoehr in new Asia-Pacific financing role', 'TABLE-India cenbank says reverse repo bids rise to 116.15 bln rupees', "BRIEF-Oceanwide terminates plan to sell unit's stakes to Minsheng Holdings", 'Law enforcement bikers fought outlaw gang in deadly Denver melee', 'Brokerage firm RCS Capital files for bankruptcy', "Indonesia's tourist arrivals drop 0.16 pct y/y in Dec", 'BRIEF-Shanghai New World gets regulatory approval to issue shares in private placement', 'A hefty earnings week ahead', 'No. 23 Oregon completes sweep in Arizona', 'Dubai Investments Q4 net profit rises 2.6 pct'], '0101': ['Dr. Paula Watkins: First African-American Virtual School Founder', "Doan breaks Coyotes' record in win vs. Jets", "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Stars rout Predators to end year in style', 'Puerto Rico reports first case of Zika virus, spread by mosquitoes', "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", "UPDATE 2-Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Clippers cap trip with win over Pelicans', 'Morpx Inc to Exhibit at 2016 International CES, Sands, Hall G - 80851', 'Germany says it has information Islamic State planned suicide attacks in Munich'], '0203': ["Qatar's Gulf International Services swings to Q4 net loss", 'Crawford carries Blackhawks past Avalanche', 'UPDATE 1-China 2015 gold output dips 0.4 pct, consumption rises', 'Brown scores twice as Kings defeat Coyotes', "Lenovo's Q3 revenue falls 8 pct to $12.9 bln; net profit beats estimates", 'Get answers to all your burning college football recruiting questions at C Spire - SuperTalk Mississippi 2016 National Signing Day event on Feb. 3', 'KFC wins China payout over mutant chicken rumors', 'SE Asia Stocks-Weak; Thai index off lows ahead of cenbank rate decision', 'DePaul takes down No. 11 Providence', 'DLF Q3 net profit up 24 percent as rental income rises'], '0303': ['China stocks firm, bolstered by property sector; Hong Kong shares dip', 'Alibaba finance arm in talks to invest in Chinese media group Caixin -sources', 'Call for government unity as Australian PM faces critical budget, election', 'UPDATE 1-Vatican cardinal denies attempts to cover up child sex abuse', 'Donald Trump Jr. appears alongside white supremacist in radio show', "FOREX-Dollar gains with Friday's US jobs data in focus", 'The Scientology Information Center Answers “What is Scientology” During Clearwater’s Blast Friday', 'Spurs run away from Detroit in win', 'Asia to see first gasoline squeeze in more than 15 years', 'Maruti Suzuki to hike car prices after new green tax']}
    return di

def make_dates(months):
    month_dict = {1:2, 2:2, 3:3}
    #return list of dates to map to other variables
    #return in the form "0101", "0102" corresponding to Jan. 1, Jan. 2...
   # month_dict = {1:31, 2:29, 3:31, 4:30}
    d_list = []
    for i in range(1,months+1):
        if i < 10:
            m = '0' + str(i)
        else:
            m = str(i)
        d = month_dict[i]
        for l in range(1,d+1):
            if l < 10:
                date = '0' + str(l)
            else:
                date = str(l)
            d_list.append(m + date)
    return d_list


def get_headlines():
    rows = []
  #  month_dict = {1:31, 2:29, 3:31, 4:30}
  #  months_test = {1:4, 2:5}
    search_url = 'http://www.reuters.com/resources/archive/us/20160123.html'
    search_base = 'http://www.reuters.com/resources/archive/us/2016'
    search_end = ".html"
    dates = make_dates(3)
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
        trunc_list = daily_headlines[0:10]
        date_headline[i] = trunc_list
    return date_headline
#    return dates

def parse_lang_dict():
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

def make_tokens():
    l = get_headlines()
    trunc_list = l[0:20]
    token_list= []

def calc_sentiment():
    #call get_headlines()
    #tokenize
    #calculate amount of positive and negative words
    l = get_headlines()
    trunc_list = l[0:20]
    #make tokens and remove everything that is all capital letters
    #observed that reuters uses all-caps for things like "UPDATE" or "BRIEF" that are not sentiment containing words but rather descriptive attributes about the content
    #anything else that is all capital letters is an abbreviation therefore also irrelevant for sentiment analysis purposes
           

if __name__ == "__main__":
    d = test_dict()
    print(d)
   # make_dates(3)
   # calc_sentiment()
   # l = get_headlines()
   # trunc_list = l[0:20]
   # for i in trunc_list:
   #     print(i)
  # x = parse_lang_dict()
  # y = x[0]
  # z = x[1]
  # print("separted tuples?")
  # for a in z:
  #      print(a)
