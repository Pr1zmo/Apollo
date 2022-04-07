"""
	
	Return a formatted fiat amount of a given amount of a fiat currency.
	
	Example: float 1000.505123 -> str $1,000.50
	Example: float 15023.00123 -> str $15,023
	
	Parameters:
		
		fiatBalance (float): The balance of a fiat currency.
		decimals (int) = 2: The amount of decimals to correct for after the decimals place.
	
	Returns:
		
		str: A formatted stirng of the fiat balance with commas, decimal point if needed, and a currency symbol.
	
"""
def getFormattedFiatBalance(fiatBalance: float, decimals: int = 2) -> str:
	
	# TODO: Add Boolean Parameter -> forceDecimalAmount: False
	# TODO: Would Force the Decimal Amount, regardless of value, to Concatenate to the Formatted String
	
	# * Force Fiat Balance Number to a Float (int Doesn't Auto Type Cast to Float)
	
	fiatBalance = float(fiatBalance)
	
	# * Initialize Basic Variables for Constructing Formatted Fiat Balance
	
	fiatBalanceString = str(fiatBalance)
	
	indexOfDecimalPoint = fiatBalanceString.index('.') 
	
	# * Check for Excess Small Amounts
	
	if (len(fiatBalanceString[(indexOfDecimalPoint + 1):]) > decimals):
		
		fiatBalanceString = fiatBalanceString[:((indexOfDecimalPoint + 1) + decimals)]
	
	newTrailingDecimalAmountString = fiatBalanceString[(indexOfDecimalPoint + 1):]
	
	# * Check if A Decimal Amount is Needed for the Final String
	
	isDecimalAmountNeeded = (int(newTrailingDecimalAmountString) != 0)
	
	if (isDecimalAmountNeeded):
		
		lengthOfNewTrailingDecimals = len(newTrailingDecimalAmountString)
		
		if (lengthOfNewTrailingDecimals < decimals):
			
			fiatBalanceString += ('0' * (decimals - lengthOfNewTrailingDecimals))
	
	else:
		
		fiatBalanceString = fiatBalanceString[:indexOfDecimalPoint]
	
	# * Add Commas Between Every 3 Digits of Whole Numbers
	
	cacheIndex = -3
	
	fiatBalanceNoDecimalsString = fiatBalanceString[:indexOfDecimalPoint]
	
	for _ in range((len(fiatBalanceNoDecimalsString) - 1) // 3):
		
		fiatBalanceNoDecimalsString = f"{fiatBalanceNoDecimalsString[:cacheIndex]},{fiatBalanceNoDecimalsString[cacheIndex:]}"
		
		cacheIndex -= 4
	
	# * Add Everything Together
	
	fiatBalanceString = (fiatBalanceNoDecimalsString + fiatBalanceString[indexOfDecimalPoint:])
	
	# * Add Currency Symbol Just for Aesthetics
	
	return ('$' + fiatBalanceString)

"""
	
	Get amount of a balance from a string that represents a fiat amount.
	
	Example: str $5,000.05 -> float 5000.05
	Example: str 5k -> float 5000.0
	
	Parameters:
		
		abstractFiatAmount (str): String of the amount.
	
	Returns:
		
		float: A fiat balance in floating point notation.
	
"""
def getFiatAmountFromAbstractString(abstractFiatAmount: str) -> float:
	
	# * str.removeprefix() Requires Python 3.9.0 or Later
	
	abstractFiatAmount = abstractFiatAmount.removeprefix('$')
	
	abstractFiatAmount = abstractFiatAmount.replace(',', '', -1)
	
	abstractFiatAmount = abstractFiatAmount.lower()
	
	FIAT_CHARS_DICT = {
		
		"k": "000",
		"m": "000000"
		
	}
	
	for fiatChar in FIAT_CHARS_DICT:
		
		abstractFiatAmount = abstractFiatAmount.replace(fiatChar, FIAT_CHARS_DICT.get(fiatChar), -1)
	
	return float(abstractFiatAmount)