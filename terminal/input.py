from types import FunctionType

from terminal.print import FrameBuilder
from utilities      import getFiatAmountFromAbstractString

"""
	
	Get an input string from the terminal.
	
	Parameters:
		
		text (str): Text to be displayed for input.
	
	Returns:
		
		str: A string of text returned after the user presses enter in the terminal.
	
"""
def getInput(text: str) -> str:
	
	return input("  " + text)

"""
	
	Method for getting a valid integer from the terminal.
	
	Parameters:
		
		text (str): Text to be displayed for input.
	
	Returns:
		
		int: A valid integer.
	
"""
def getInputInteger(text: str) -> int:
	
	try:
		
		return int(getInput(text))
	
	except ValueError:
		
		invalidIntegerFrame = FrameBuilder(isDoubleLine = False)
		
		invalidIntegerFrame.addCenteredTextLine("Invalid Integer")
		
		invalidIntegerFrame.printFrame()
		
		print()
		
		return getInputInteger(text)

"""
	
	Get a valid integer above 0.
	
	Parameters:
		
		text (str): Text to be displayed for the input.
	
	Returns:
		
		int: A valid integer above 0.
	
"""
def getInputPositiveIntegerAbove0(text: str) -> int:
	
	inputInteger = getInputInteger(text)
	
	if (inputInteger <= 0):
		
		return getInputPositiveIntegerAbove0(text)
	
	else:
		
		return inputInteger

"""
	
	Method for getting a valid float from the terminal.
	
	Parameters:
		
		text (str): Text to be displayed for input.
	
	Returns:
		
		float: A valid float.
	
"""
def getInputFloat(text: str) -> float:
	
	try:
		
		return float(getInput(text))
	
	except ValueError:
		
		invalidFloatFrame = FrameBuilder(isDoubleLine = False)
		
		invalidFloatFrame.addCenteredTextLine("Invalid Float")
		
		invalidFloatFrame.printFrame()
		
		print()
		
		return getInputFloat(text)

"""
	
	Get a valid float above 0.0.
	
	Parameters:
		
		text (str): Text to be displayed for the input.
	
	Returns:
		
		float: A valid float above 0.0.
	
"""
def getInputPositiveFloatAbove0(text: str) -> float:
	
	inputFloat = getInputFloat(text)
	
	if (inputFloat <= 0.0):
		
		return getInputPositiveFloatAbove0(text)
		
	else:
		
		return inputFloat

"""
	
	Method for getting a valid fiat amount.
	
	Parameters:
		
		text (str): Text to be displayed for input.
	
	Returns:
		
		float: A valid float of a fiat balance.
	
"""
def getInputFiatAmount(text: str) -> float:
	
	try:
		
		return getFiatAmountFromAbstractString(getInput(text))
	
	except ValueError:
		
		return getInputFiatAmount(text)

"""
	
	Get a valid fiat amount above 0.0.
	
	Parameters:
		
		text (str): Text to be displayed for input.
	
	Returns:
		
		float: A valid float of a fiat balance above 0.0.
	
"""
def getInputPositiveFiatAmountAbove0(text: str) -> float:
	
	inputFiatAmount = getInputFiatAmount(text)
	
	if (inputFiatAmount <= 0.0):
		
		return getInputPositiveFiatAmountAbove0(text)
	
	else:
		
		return inputFiatAmount

"""
	
	Method for getting a valid yes or no input.
	
	Parameters:
		
		question (str): Question to be displayed for input.
	
	Returns:
		
		bool: True if input is equal to y or yes, else False.
	
"""
def getInputYN(question: str) -> bool:
	
	VALID_RESPONSES = ["y", "yes", "n", "no"]
	
	inputResponse = getInput(question + " (Y/N): ").lower()
	
	if (inputResponse not in VALID_RESPONSES):
		
		return getInputYN(question)
	
	else:
		
		return ((inputResponse == VALID_RESPONSES[0]) or (inputResponse == VALID_RESPONSES[1]))


"""
	
	Class to handle the executing of commands. These commands are a 
	representation of a function, and it's corresponing name(s).
	
"""
class CommandsManager(dict):
	
	def addCommands(self, function: FunctionType, *args):
		
		for command in args:
			
			self[command] = function
	
	def executeCommand(self, command: str, *args):
		
		try:
			
			if (args == ()):
				
				self[command]()
			
			else:
				
				self[command](*args)
		
		except KeyError:
			
			invalidCommandFrame = FrameBuilder()
			
			invalidCommandFrame.addCenteredTextLine("Invalid Command")
			
			invalidCommandFrame.printFrame()