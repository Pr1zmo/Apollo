"""
	
	Class that's used for holding market history data to be used for ApolloAI.
	This holds both the actual market data formatted from the CoinGeckoAPI, as 
	well as metadata related to info about the crypto.
	
	Parameters:
		
		cryptoName (str): The name of a cryptocurrency.
		cryptoSymbol (str): The symbol of a cryptocurrency.
		unformattedCoinGeckoData (dict): A python encoded dictionary of the unformatted data from the CoinGecko API.
	
"""
class MarketHistory(dict):
	
	def __init__(self, cryptoName: str, cryptoSymbol: str, unformattedCoinGeckoData: dict):
		
		self["meta"] = {
			
			"name":   cryptoName.title(),
			"symbol": cryptoSymbol.lower()
			
		}
		
		epochList       = []
		priceList       = []
		totalVolumeList = []
		marketCapList   = []
		
		for pricePair in unformattedCoinGeckoData.get("prices"):
			
			# * The Reason Why the Last 3 Digits Aren't Used is Because
			# * The Python datetime Library Doesn't Support Them for Some Reason :(
			
			epochList.append(int(str(pricePair[0])[:-3]))
			priceList.append(pricePair[1])
		
		for totalVolumePair in unformattedCoinGeckoData.get("total_volumes"):
			
			totalVolumeList.append(totalVolumePair[1])
		
		for marketCapPair in unformattedCoinGeckoData.get("market_caps"):
			
			marketCapList.append(marketCapPair[1])
		
		self["data"] = []
		
		for i in range(len(epochList)):
			
			self.get("data").append({
				
				"epoch":       epochList[i],
				"price":       priceList[i],
				"marketCap":   marketCapList[i],
				"totalVolume": totalVolumeList[i]
				
			})