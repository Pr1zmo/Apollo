"""
	
	Main indicator to be used by ApolloAI. A simple moving average is a common
	indicator used by technical anaylists and traders as a metric for averaging
	prices from a given interval. This is useful as it mitigates risk, but doesn't
	rely on a total average, or an average over an incredibly long period of time
	that might be more common with investing.
	
	Parameters:
		
		intervalInHoursToAverage (int): How many hours to average from the last hour.
	
"""
class SimpleMovingAverage():
	
	intervalInHoursToAverage: int
	
	simpleMovingAverageLog: list
	
	lastSMA: float
	
	def __init__(self, intervalInHoursToAverage: int):
		
		self.intervalInHoursToAverage = intervalInHoursToAverage
		
		self.simpleMovingAverageLog = []
	
	"""
		
		Update the current moving average.
		
	"""
	def update(self, marketLog: list):
		
		lengthOfMarketLog = len(marketLog)
		
		cacheTotal = 0
		
		if (lengthOfMarketLog > self.intervalInHoursToAverage):
			
			for i in range((-self.intervalInHoursToAverage - 1), -1):
				
				cacheTotal += marketLog[i]["price"]
			
			self.lastSMA = (cacheTotal / self.intervalInHoursToAverage)
			
		else:
			
			for marketInfo in marketLog:
				
				cacheTotal += marketInfo["price"]
			
			self.lastSMA = (cacheTotal / lengthOfMarketLog)
		
		self.simpleMovingAverageLog.append(self.lastSMA)