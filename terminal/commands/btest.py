from coingecko.api     import getDataFromSymbol, getNameFromSymbol
from terminal.input    import getInput, getInputPositiveFiatAmountAbove0, getInputPositiveFloatAbove0, getInputPositiveIntegerAbove0
from ai.ai             import ApolloAI
from ai.market_history import MarketHistory
from terminal.print    import println, FrameBuilder
from terminal.theme    import fg
from plot.plot         import plotTransactionData
from utilities         import getFormattedFiatBalance

"""
	
	Command for using the ApolloAI for backtesting cryptocurrency data from CoinGecko.
	
"""
def executeCommandBTest():
    
	print()
	
	inputCryptoSymbol = getInput("Enter Cryptocurrency Symbol (Ex. BTC): ")
	
	cryptoName = getNameFromSymbol(inputCryptoSymbol)
	
	if (cryptoName == ""):
		
		print()
		println("Invalid Cryptocurrency Symbol! Try Again...")
		
		return executeCommandBTest()
	
	inputAmountOfDays           = getInputPositiveIntegerAbove0(fg("magenta_2b") + "Enter Amount of Days to Get Data (Max 30): ")
	inputBudget                 = getInputPositiveFiatAmountAbove0(fg("aquamarine_1b") + "Enter Budget ($USD): ")
	inputStartingBufferInterval = getInputPositiveIntegerAbove0(fg("medium_purple_2a") + "Enter Simple Moving Average Start Buffer Interval (10+): ")
	inputBuyMarginPercentage    = getInputPositiveFloatAbove0(fg("green") + "Enter Buy Margin Percentage (Ex: 1.6): ")
	inputProfitMarginPercentage = getInputPositiveFloatAbove0(fg("red") + "Enter Profit Margin Percentage (Ex: 1.75): ")
	inputSMAInterval            = getInputPositiveIntegerAbove0(fg("dark_orange") + "Enter Simple Moving Average Interval (2+): ")
	
	apolloAI = ApolloAI(inputBudget, inputStartingBufferInterval, inputBuyMarginPercentage, inputProfitMarginPercentage, inputSMAInterval)
	
	marketHistory = MarketHistory(cryptoName, inputCryptoSymbol, getDataFromSymbol(inputCryptoSymbol, inputAmountOfDays))
	
	apolloAI.backTest(marketHistory)
	
	transactionsFrame = FrameBuilder("Apollo Transactions")
	
	for transaction in apolloAI.transactionLog:
		
		# * Sell
		
		if (transaction["transactionType"]):
			
			typeString = "SELL"
			typeColor  = fg("red")
		
		# * Buy
		
		else:
			
			typeString = "BUY"
			typeColor  = fg("green")
		
		transactionsFrame.addTextLine(f"Date & Time: {transaction['dateTime']}", fg("magenta_2b"))
		transactionsFrame.addTextLine(f"{typeString}: {transaction['amount']} at {getFormattedFiatBalance(transaction['price'])}", typeColor)
		transactionsFrame.addTextLine(f"Money Balance: {getFormattedFiatBalance(transaction['moneyBalance'])}", fg("medium_purple_2a"))
		transactionsFrame.addTextLine(f"Total Profit: {getFormattedFiatBalance(transaction['totalProfit'])}", fg("light_green_3"))
		transactionsFrame.addTextLine(f"Coin Balance: {transaction['coinBalance']}", fg("dark_orange"))
		
		# * Check if Current Transaction is the Last to Be Printed for the Transaction Frame
		
		if (apolloAI.transactionLog.index(transaction) != (len(apolloAI.transactionLog) - 1)):
			
			transactionsFrame.addWhitespaceLine()
	
	transactionsFrame.printFrame()
	
	# * Display Matplotlib GUI of Market History, Simple Moving Average Indicator, and Transaction Log
	
	plotTransactionData(marketHistory, apolloAI.indicatorSimpleMovingAverage.simpleMovingAverageLog, apolloAI.transactionLog)
