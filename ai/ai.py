from ai.market_history  import MarketHistory
from arithmetic         import getPercentage
from ai.transaction_log import TransactionLog
from ai.indicator       import SimpleMovingAverage

"""
	
	ApolloAI class is the actual brain of the program. This class has many methods
	which are used for the purpose of buying and selling a given cryptocurrency.
	
	A backtest method is supplied as a way of testing the AI with any given data.
	This method emulates real world trading, and prevents the AI from being able to
	know the future as every iteration over a list of market history data, the AI
	will decide whether or not to buy/sell.
	
	Parameters:
		
		budget (float): A float of a balance for the AI to use.
		intervalStartingBuffer (int): The integer for the initial interval to wait to see how volatile the market is.
		marginBelowSMABeforeBuy (float): The percentage to buy below the simple moving average.
		marginBeforeSell (float): The percentage to sell above the simple moving average.
		intervalForSimpleMovingAverage (int): The interval to average the last prices.
	
"""
class ApolloAI():
	
	intervalStartingBuffer: int
	
	marginBelowSMABeforeBuy: float
	marginBeforeSell:        float
	
	intervalForSimpleMovingAverage: int
	
	transactionLog: TransactionLog
	
	marketLog: list
	
	indicatorSimpleMovingAverage: SimpleMovingAverage
	
	def __init__(self,
				budget: float,
				intervalStartingBuffer: int,
				marginBelowSMABeforeBuy: float,
				marginBeforeSell: float,
				intervalForSimpleMovingAverage: int):
		
		self.intervalStartingBuffer = intervalStartingBuffer
		
		self.marginBelowSMABeforeBuy = marginBelowSMABeforeBuy
		self.marginBeforeSell        = marginBeforeSell
		
		self.transactionLog = TransactionLog(budget)
		
		self.marketLog = []
		
		self.indicatorSimpleMovingAverage = SimpleMovingAverage(intervalForSimpleMovingAverage)
	
	def backTest(self, marketHistory: MarketHistory):
		
		for marketInfo in marketHistory.get("data"):
			
			self.addNewMarketInfo(marketInfo)
	
	"""
		
		When this method is called, the AI has to decide whether it is a good time to buy, sell, or wait.
		
	"""
	def addNewMarketInfo(self, newMarketInfo: dict):
		
		self.marketLog.append(newMarketInfo)
		
		self.indicatorSimpleMovingAverage.update(self.marketLog)
		
		if (self.intervalStartingBuffer != 0):
			
			self.intervalStartingBuffer -= 1
			
			return
		
		newPrice = int(newMarketInfo["price"])
		
		if (self.checkForBuy(newPrice)):
			
			self.transactionLog.addTransaction(newMarketInfo["epoch"], False, self.getAmountToBuy(newPrice), newPrice)
		
		elif (self.checkForSell(newPrice)):
			
			self.transactionLog.addTransaction(newMarketInfo["epoch"], True, self.getAmountToSell(newPrice), newPrice)
	
	def checkForBuy(self, lastPrice: float) -> bool:
		
		if (self.transactionLog.moneyBalance > lastPrice):
			
			return ((getPercentage(lastPrice, self.indicatorSimpleMovingAverage.lastSMA) - 100) <= -self.marginBelowSMABeforeBuy)
		
		else:
			
			return False
	
	def checkForSell(self, lastPrice: float) -> bool:
		
		if (self.transactionLog.coinBalance > 0):
			
			return ((getPercentage(lastPrice, self.transactionLog.lastBoughtPrice) - 100) >= self.marginBeforeSell)
		
		else:
			
			return False
	
	# ! For the Future, Handle Prices as a Float
	
	def getAmountToBuy(self, price: float):
		
		return (self.transactionLog.moneyBalance // price)
	
	def getAmountToSell(self, price: float):
		
		return self.transactionLog.coinBalance
