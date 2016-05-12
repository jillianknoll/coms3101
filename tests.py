import unittest as unit
import main
from main import InputZeroException as exc

global test_dict 
test_dict = {'0102': ['Raptors get win as Hornets scoring dries up in final minutes', 'Buffalo Bills - PlayerWatch', 'Bulls win laugher vs. Knicks', 'Florida coach Gallant gets contract extension', 'Raptors take control late to beat Hornets', 'McCaffrey sets Rose Bowl records in Stanford rout', "UPDATE 1-Bill Cosby's wife must testify in civil case against him, judge rules", 'Heat look on the Whiteside in 106-82 win', 'NIMBLE STORAGE SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: Kahn Swick &amp; Foti, LLC Reminds Investors With Losses in Excess of $100,000 of Lead Plaintiff Deadline in Class Action Lawsuit Against Nimble Storage, Inc', 'Laos, Hmong Community, Veterans Reflect Upon Efforts in Washington, U.S. Congress'], '0104': ['Asian bankers will shift from deals to distress', 'Seahawks shut down Cardinals', 'Top 25 roundup: Cal hands Utah 2nd loss in row', 'Manning returns to help Broncos earn AFC top seed', 'BRIEF-Shenzhen Worldunion Properties Consultancy terminates acquisition plan', 'Operation to flush out Indian air base attackers enters second night', 'BRIEF-Jiangsu JiuJiuJiu Technology unit to recall syrup', "Indonesia's tourist arrivals rise 1.70 pct y/y in Nov", 'BRIEF-Nanfang Black Sesame to acquire edible oil firm for 625 mln yuan', 'Colorado 56, Stanford 55'], '0302': ['Indiana edges Iowa to seal outright Big Ten title', 'CORRECTED-HKEx 2015 profit surges 54 pct to record high as trading volumes rise', 'Australia softens sanctions against Iran', 'Chinese overseas investment tops $1 trillion over a decade - report', 'Chongqing blazes economic trail as Bo scandal recedes', 'LME revenue from trading fees, tariffs surges 51 pct in 2015', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'Parts of Great Barrier Reef face permanent destruction due to El Nino - scientists', 'China stocks surge, led by property shares; Hong Kong follows global rally', 'BRIEF-United Bank For Africa appoints Kennedy Uzoka as group MD/CEO'], '0204': ['ViaCyte Acquires Rights to BetaLogics Assets, Expanding and Extending Industry-Leading Portfolio for Stem Cell-Derived Approaches to Type 1 Diabetes', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'Primero Receives Legal Claim Filed by Mexican Tax Authorities', 'No. 7 Kansas overcomes slow start, beats Kansas State', 'China, HK stocks rebound as dollar tumble ease yuan depreciation fears', 'Indonesia 2016 rubber exports seen declining at least 8 pct -industry assoc', 'Hornets beat LeBron for first time since 2010', 'Whiteside returns to help Heat defeat Mavericks', 'U.S. House panel subpoenas hacked federal agency for documents', 'MIDEAST STOCKS - Factors to watch - Feb 4'], '0202': ["BRIEF-Indonesia's XL Axiata eyes funds from rights offer, tower sale", 'UPDATE 3-Bernie Sanders shows strong momentum on social media', 'Lawyers from Keller Rohrback Share Nobel Peace Prize Nomination', "Malaysia's central bank to launch new Islamic T-bills this week", 'BRIEF-Tiger Branded Consumer Goods Q1 loss before tax 975.3 mln naira', 'Oilers hope returning McDavid can stop them slipping further', 'BRIEF-Henan Kedi Dairy Industry to issue shares as 2015 dividend', "Broncos' Manning says no decision yet on retirement", 'BRIEF-Yunnan Hongxiang Yixintang Pharma sells stake in Kunming-based pharma co', 'BRIEF-Yunnan Hongxiang Yixintang Pharma buys Zhengzhou-based co'], '0205': ['Toews nets OT winner for Blackhawks', 'Rockets finsih strong in win vs. Suns', 'USC 80, UCLA 61', "BRIEF-Vietnam's Military Bank says 2015 net profit up 0.8 pct y/y", 'Oil falls 2 pct as producer meet uncertainty offsets weak dollar', 'Indian lenders, central bank, square off over cash shortages', 'China money rates steady ahead of Lunar New Year festival on c.bank injections', 'Eberle leads Oilers in rout of Senators', 'Mosquito repellant sales boom in Brazil amid Zika scare', "Doubting India's 'fastest-growing' GDP stats, economists devise their own"], '0103': ['Davis paces Pelicans past Mavericks', 'San Diego State 70, Utah State 67', 'Spurs ground Rockets to stay unbeaten in San Antonio', 'Bucks 95, Timberwolves 85', 'MIDEAST STOCKS - Factors to watch - Jan 3', 'Stream TV Networks to Exhibit at CES Unveiled Las Vegas 2016, Booth 13633', 'New Mexico 77, Fresno State 62', 'George carries Pacers past Pistons', 'Cavaliers defeat Magic for 13th straight time', "Blue Jackets' rookie goalie stops Capitals in shootout"], '0301': ['Venture+ Forum at HIMSS16 Annual Conference Announces Four Companies Advancing to Final Pitch Competition', 'Datsyuk lifts Red Wings past Stars in OT', 'Mexico says 11 pregnant women infected with Zika', 'Schenn hat trick helps Flyers defeat Flames', 'CORRECTED-Taiwan stocks up tracking overseas markets; main index at 3-mth high', "Fitch Affirms Finnet Indonesia at 'A(idn)'; Stable Outlook", "Olympics-Gatlin's coach steps down as U.S. relay boss for Rio", "Indonesia's foreign tourist arrivals rise 2.2 pct y/y in Jan", "Brazil's Petrobras corruption investigation targets Lula", 'China court jails 24 over $1.5-bln financial fraud - Xinhua'], '0201': ['MOVES-Credit Suisse hires Stoehr in new Asia-Pacific financing role', 'TABLE-India cenbank says reverse repo bids rise to 116.15 bln rupees', "BRIEF-Oceanwide terminates plan to sell unit's stakes to Minsheng Holdings", 'Law enforcement bikers fought outlaw gang in deadly Denver melee', 'Brokerage firm RCS Capital files for bankruptcy', "Indonesia's tourist arrivals drop 0.16 pct y/y in Dec", 'BRIEF-Shanghai New World gets regulatory approval to issue shares in private placement', 'A hefty earnings week ahead', 'No. 23 Oregon completes sweep in Arizona', 'Dubai Investments Q4 net profit rises 2.6 pct'], '0101': ['Dr. Paula Watkins: First African-American Virtual School Founder', "Doan breaks Coyotes' record in win vs. Jets", "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Stars rout Predators to end year in style', 'Puerto Rico reports first case of Zika virus, spread by mosquitoes', "Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", "UPDATE 2-Wayne Rogers, Trapper John on TV's 'M*A*S*H', dies at 82", 'Clippers cap trip with win over Pelicans', 'Morpx Inc to Exhibit at 2016 International CES, Sands, Hall G - 80851', 'Germany says it has information Islamic State planned suicide attacks in Munich'], '0203': ["Qatar's Gulf International Services swings to Q4 net loss", 'Crawford carries Blackhawks past Avalanche', 'UPDATE 1-China 2015 gold output dips 0.4 pct, consumption rises', 'Brown scores twice as Kings defeat Coyotes', "Lenovo's Q3 revenue falls 8 pct to $12.9 bln; net profit beats estimates", 'Get answers to all your burning college football recruiting questions at C Spire - SuperTalk Mississippi 2016 National Signing Day event on Feb. 3', 'KFC wins China payout over mutant chicken rumors', 'SE Asia Stocks-Weak; Thai index off lows ahead of cenbank rate decision', 'DePaul takes down No. 11 Providence', 'DLF Q3 net profit up 24 percent as rental income rises'], '0303': ['China stocks firm, bolstered by property sector; Hong Kong shares dip', 'Alibaba finance arm in talks to invest in Chinese media group Caixin -sources', 'Call for government unity as Australian PM faces critical budget, election', 'UPDATE 1-Vatican cardinal denies attempts to cover up child sex abuse', 'Donald Trump Jr. appears alongside white supremacist in radio show', "FOREX-Dollar gains with Friday's US jobs data in focus", 'The Scientology Information Center Answers “What is Scientology” During Clearwater’s Blast Friday', 'Spurs run away from Detroit in win', 'Asia to see first gasoline squeeze in more than 15 years', 'Maruti Suzuki to hike car prices after new green tax']}

global mini_dict
mini_dict = {'0101':['good 1000 ^^^^ $$$$$m 8sjdfj168']}

global sentiment_result
sentiment_result = {'0102': 0.75, '0202': 0.2, '0203': -0.1111111111111111, '0204': -0.42857142857142855, '0101': -0.5555555555555556, '0201': -0.6, '0302': 0.3333333333333333, '0104': 0.0, '0103': 1.0, '0205': 0.3333333333333333, '0301': -0.3333333333333333, '0303': 0.14285714285714285}

global zero_dict
zero_dict = {'0101':['000 baaa &&& ew table'], '0102':['000 lawl &##&& ew chair']}

global token_result
token_result = {'0101': ['the', 'girl', 'wne', 't', 'walk', 'blah', 'ha', 'dah'], '0202': ['test', 'test', 'test', 'testtest', 'mytest', 'hello', 'there']}

global token_input
token_input = {'0101':['The girl wne t <> on7879 walk', 'Blah ha !f25tsdf dah'], '0202':['test test test test.test', 'my.test ^^^ $$$ hello there']}

global token_bad_input
token_bad_input = {'0101':['&&& *** ((( ### !!!'], '2020': ['~~~ &&& 7number8']}

global token_bad_result
token_bad_result = {'2020': [], '0101': []}

class Test(unit.TestCase):

	def test_dates(self):
		"""tests the make_dates function in main.py"""
		month_dict = {1:2, 2:2, 3:3}
		result = main.make_dates(3,month_dict)
		correct = ['0101', '0102', '0201', '0202', '0301', '0302', '0303']
		self.assertEqual(result, correct)

	def test_sentiment(self):
		"""tests the calc_sentiment function in main.py with a robust test dictionary"""
		global sentiment_result
		global test_dict
		result = main.calc_sentiment(test_dict)
		self.assertEqual(result,sentiment_result)

	def test_sentiment2(self):
		"""tests the calc_sentiment function in main.py with a numerical dictionary with one alpha character"""
		sentiment_result = {'0101':1}
		global mini_dict
		result = main.calc_sentiment(mini_dict)
		self.assertDictEqual(result,sentiment_result)

	def test_sentiment0(self):
		"""tests the calc_sentiment function in main.py with a dictionary that should return 0"""
		sentiment_result = {'0101':0, '0102':0}
		global zero_dict
		result = main.calc_sentiment(zero_dict)
		self.assertEqual(result,sentiment_result)

	def test_tokens(self):
		"""tests the make_token function in main.py with a dictionary containing some non alpha characters"""
		global token_result
		global token_input
		result = main.make_tokens(token_input)
		self.assertEqual(result,token_result)

	def test_token_bad_input(self):
		"""tests the make_token function in main.py with a dictionary containing some non alpha characters. The make_tokens function should create an empty dictionary"""
		global token_bad_input
		global token_bad_result
		result = main.make_tokens(token_bad_input)
		self.assertEqual(result,token_bad_result)

	#write four more tests you can do it
	def test_exception_zero(self):
		"""make_dates should throw an InputZeroException"""
		try: 
			main.make_dates(0, {'0101':['1','2']})
		except main.InputZeroException:
			self.assertTrue(True)
		else:
			self.fail

	def test_exception_invalid_input(self):
		"""make_dates should throw an InvalidInputException"""
		try: 
			main.make_dates('a', {'0101':['1','2']})
		except main.InvalidInputException:
			self.assertTrue(True)
		else:
			self.fail

	def test_exception_invalid_input_tokens(self):
		"""make_dates should throw an InvalidInputException"""
		try: 
			main.make_tokens('a')
		except main.NonDictionaryInputException:
			self.assertTrue(True)
		else:
			self.fail

	def test_exception_invalid_input_sentiment(self):
		"""calc_sentiment should throw an InvalidInputException"""
		try: 
			main.calc_sentiment('a')
		except main.NonDictionaryInputException:
			self.assertTrue(True)
		else:
			self.fail

	def test_exception_invalid_input_sentiment(self):
		"""calc_sentiment should throw an InvalidInputException"""
		try: 
			main.calc_sentiment('a')
		except main.NonDictionaryInputException:
			self.assertTrue(True)
		else:
			self.fail

	def test_exception_file_overwrite(self):
		"""calc_sentiment should throw an InvalidInputException"""
		try: 
			main.write_csv()
		except main.FileOverwriteException:
			self.assertTrue(True)
		else:
			self.fail






if __name__ == '__main__':
	unit.main()
