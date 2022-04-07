import matplotlib.pyplot as matplot
import numpy

from ai.market_history  import MarketHistory
from ai.transaction_log import TransactionLog
from utilities          import getFormattedFiatBalance

"""
	
	Method for using the library MatPlotLib to display ApolloAI's data.
	It displays lines and points for prices, hour intervals, as well as buy's and sell's.
	
	Parameters:
		
		marketHistory (MarketHistory): The Market History of a CryptoCurrency from CoinGecko.
		simpleMovingAverageLog (list): A list of moving averages supplied by the SMA indicator.
		transactionLog (TransactionLog): A log of transactions.
	
"""
def plotTransactionData(marketHistory: MarketHistory, simpleMovingAverageLog: list, transactionLog: TransactionLog):
	
	plotTitle = f"Apollo AI Transactions vs {marketHistory['meta']['name']} Price\n" + \
				f"Transactions: {len(transactionLog)} | Total Profit: {getFormattedFiatBalance(transactionLog.totalProfit)}"
	
	matplot.title(plotTitle)
	matplot.xlabel("Hours")
	matplot.ylabel("Price (USD)")
	
	epochList     = []
	priceList     = []
	marketCapList = []
	volumeList    = []
	
	for marketInfo in marketHistory.get("data"):
		
		epochList.append(marketInfo["epoch"])
		priceList.append(marketInfo["price"])
		marketCapList.append(marketInfo["marketCap"])
		volumeList.append(marketInfo["totalVolume"])
	
	marketHistoryRangeNumpyArray = numpy.array(range(1, (len(marketHistory.get("data")) + 1)))
	
	matplot.plot(marketHistoryRangeNumpyArray, priceList, label = "Price")
	
	matplot.plot(marketHistoryRangeNumpyArray, simpleMovingAverageLog, label = "Simple Moving Average")
	
	buyMarkers  = [[], []]
	sellMarkers = [[], []]
	
	for transaction in transactionLog:
		
		# * Sell
		
		if (transaction["transactionType"]):
			
			sellMarkers[0].append(epochList.index(transaction["epoch"]) + 1)
			sellMarkers[1].append(transaction["price"])
		
		# * Buy
		
		else:
			
			buyMarkers[0].append(epochList.index(transaction["epoch"]) + 1)
			buyMarkers[1].append(transaction["price"])
	
	matplot.plot(buyMarkers[0],  buyMarkers[1],  "o", color = "green", label = "Buy")
	matplot.plot(sellMarkers[0], sellMarkers[1], "o", color = "red",   label = "Sell")
	
	matplot.legend()
	
	matplot.show()
	
	matplot.clf()
	matplot.cla()
	matplot.close()
