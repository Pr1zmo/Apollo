from datetime import datetime

"""
	
	Transaction log class used by ApolloAI. This class keeps track of all transactions
	by the ai. Information kept includes: date and time, type, amount, price, money balance, 
	total profit, and coin balance.
	
	Parameters:
		
		epoch (int): An integer representation of the time that has passed since 00:00:00 UTC January 1, 1970.
		transactionType (bool): Sell is true, buy is false.
		amount (int): The amount of cryptocurrency to buy. (This will be updated to a float in the future).
		price (float): The price at which to buy an amount of the cryptocurrency.
	
"""
class TransactionLog(list):
	
	budget:       float
	moneyBalance: float
	totalProfit:  float
	coinBalance:  int
	
	lastBoughtPrice: float
	
	def __init__(self, budget: float):
		
		self.budget	      = budget
		self.moneyBalance = budget
		self.totalProfit  = 0.0
		self.coinBalance  = 0
		
		self.lastBoughtPrice = 0.0
	
	def addTransaction(self, epoch: int, transactionType: bool, amount: int, price: float):
		
		# * Sell
		
		if (transactionType):
			
			self.moneyBalance += (amount * price)
			self.totalProfit  =  (self.moneyBalance - self.budget)
			self.coinBalance  -= amount
		
		# * Buy
		
		else:
			
			self.moneyBalance -= (amount * price)
			self.coinBalance  += amount
			
			self.lastBoughtPrice = price
		
		self.append({
			
			"epoch":           epoch,
			"dateTime":        datetime.utcfromtimestamp(epoch).strftime("%m/%d/%y %I:%M:%S %p"),
			"transactionType": transactionType,
			"amount":          amount,
			"price":           price,
			"moneyBalance":    self.moneyBalance,
			"totalProfit":     self.totalProfit,
			"coinBalance":     self.coinBalance
			
		})