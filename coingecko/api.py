import requests
import json

COINGECKO_API_BASE_URL = "https://api.coingecko.com/api/v3/"

cacheCoinListData = {}

"""
	
	Method for retrieving a list of coins and their ID's to be used for the API.
	After getting the data, a cache of the data is stored to prevent abuse.
	
	Returns:
		
		dict: A dictionary loaded from the JSON of the CoinGecko API call to 
		retrieve a list of coins.
	
"""
def getCoinList() -> dict:
	
	try:
		
		coinListData = requests.get(COINGECKO_API_BASE_URL + "coins/list")
		
		coinListData.close()
		
		return json.loads(coinListData.text)
	
	except requests.RequestException:
		
		return {}

"""
	
	A method for checking if the cache is empty. All API methods in this file 
	should call this method before attempting to use the API to prevent errors.
	
	Returns:
		
		bool: True if API is good and cache is updated, else False if there's exceptions.
	
"""
def checkForEmptyCoinListCache() -> bool:
	
	global cacheCoinListData
	
	if (cacheCoinListData == {}):
		
		try:
			
			cacheCoinListData = getCoinList()
		
		except requests.RequestException:
			
			return False
		
		except requests.ConnectionError:
			
			return False
	
	return True

"""
	
	Get price data of a given cryptocurrency symbol.
	
	Parameters:
		
		symbol (str): Cryptocurrency symbol.
		days (int): Number of days to get data. (max is 30).
	
	Returns:
		
		dict: A dictionary of price, total volume, and market cap data.
	
"""
def getDataFromSymbol(symbol: str, days: int) -> dict:
	
	if (checkForEmptyCoinListCache()):
		
		coinID = getIDFromSymbol(symbol)
		
		priceData = requests.get(COINGECKO_API_BASE_URL + f"coins/{coinID}/market_chart?id={coinID}&vs_currency=usd&days={days}")
		
		priceData.close()
		
		return json.loads(priceData.text)
	
	return {}

"""
	
	Get the universal CoinGecko API ID for a given cryptocurrency symbol.
	
	Parameters:
		
		symbol (str): Cryptocurrency symbol.
	
"""
def getIDFromSymbol(symbol: str) -> str:
	
	if (checkForEmptyCoinListCache()):
		
		for coinInfo in cacheCoinListData:
			
			if (coinInfo.get("symbol") == symbol.lower()):
				
				return coinInfo.get("id")
	
	return ""

"""
	
	Get the official name of a cryptocurrency from it's symbol.
	
	Parameters:
		
		symbol (str): Cryptocurrency symbol.
	
"""
def getNameFromSymbol(symbol: str) -> str:
	
	if (checkForEmptyCoinListCache()):
		
		for coinInfo in cacheCoinListData:
			
			if (coinInfo.get("symbol") == symbol.lower()):
				
				return coinInfo.get("name")
	
	return ""
