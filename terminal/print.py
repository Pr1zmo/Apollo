
# coding: utf-8

# * Above Line Ensures the Encoding of the Current File is UTF-8
# * This is for the Special Characters for the Banner

import random

from terminal.theme import TerminalTheme
from arithmetic     import getRoundedUp

TERMINAL_THEME = TerminalTheme("Mana")

"""
	
	Print text on it's own line with an indent.
	
	Parameters:
		
		text (str): Text to be printed

"""
def println(text: str):
	
	print("  " + text)

"""
	
	Print the main menu when the terminal is shown.
	
"""
def printMainMenu():
	
	print(TERMINAL_THEME.banner)
	
	println(" █████╗ ██████╗  ██████╗ ██╗     ██╗      ██████╗      █████╗ ██╗")
	println("██╔══██╗██╔══██╗██╔═══██╗██║     ██║     ██╔═══██╗    ██╔══██╗██║")
	println("███████║██████╔╝██║   ██║██║     ██║     ██║   ██║    ███████║██║")
	println("██╔══██║██╔═══╝ ██║   ██║██║     ██║     ██║   ██║    ██╔══██║██║")
	println("██║  ██║██║     ╚██████╔╝███████╗███████╗╚██████╔╝    ██║  ██║██║")
	println("╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝")
	
	printInfoFrame()
	
	printQuoteFrame()
	
	printCommandsFrame()

"""
	
	Print information about this program.
	
"""
def printInfoFrame():
	
	apolloInfoFrame = FrameBuilder("Information")
	
	apolloInfoFrame.addKeyValuePairLine("VERSION   ", "Beta 1.0.1 Free")
	apolloInfoFrame.addKeyValuePairLine("BUILD DATE", "January 31, 2022")
	apolloInfoFrame.addKeyValuePairLine("DEVELOPER ", "Pr1zmo")
	apolloInfoFrame.addKeyValuePairLine("MOTTO     ", "Concordia Res Parvae Crescent")
	
	apolloInfoFrame.printFrame()

"""
	
	Print a random quote by famous philosophers.
	
"""
def printQuoteFrame():
	
	AUTHORS = [
		
		"Marcus Aurelius",
		"Epictetus",
		"Benjamin Franklin"
		
	]
	
	MARCUS_AURELIUS   = 0
	EPICTETUS         = 1
	BENJAMIN_FRANKLIN = 2
	
	QUOTES_LIST = [
		
		[MARCUS_AURELIUS, "In a little while you will have forgotten everything; in a little while everything will have forgotten you"],
		[MARCUS_AURELIUS, "You have power over your mind - not outside events. Realize this, and you will find strength"],
		[MARCUS_AURELIUS, "The happiness of your life depends upon the quality of your thoughts"],
		[MARCUS_AURELIUS, "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth."],
		[MARCUS_AURELIUS, "Waste no more time arguing about what a good man should be. Be one"],
		[MARCUS_AURELIUS, "When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love ..."],
		[MARCUS_AURELIUS, "If you are distressed by anything external, the pain is not due to the thing itself, but to your estimate of it; and this you have the power to revoke at any moment"],
		[MARCUS_AURELIUS, "Accept the things to which fate binds you, and love the people with whom fate brings you together, but do so with all your heart."],
		[MARCUS_AURELIUS, "The best revenge is to be unlike him who performed the injury."],
		[MARCUS_AURELIUS, "It is not death that a man should fear, but he should fear never beginning to live"],
		[MARCUS_AURELIUS, "The soul becomes dyed with the colour of its thoughts"],
		[MARCUS_AURELIUS, "Our life is what our thoughts make it"],
		[MARCUS_AURELIUS, "If someone is able to show me that what I think or do is not right, I will happily change, for I seek the truth, by which no one was ever truly harmed. It is the person who continues in his self-deception and ignorance who is harmed."],
		
		[EPICTETUS, "We should always be asking ourselves: \"Is this something that is, or is not, in my control?\""],
		[EPICTETUS, "If anyone tells you that a certain person speaks ill of you, do not make excuses about what is said of you but answer, \"He was ignorant of my other faults, else he would not have mentioned these alone"],
		[EPICTETUS, "Don't explain your philosophy. Embody it."],
		[EPICTETUS, "There is only one way to happiness and that is to cease worrying about things which are beyond the power or our will."],
		[EPICTETUS, "Man is not worried by real problems so much as by his imagined anxieties about real problems"],
		[EPICTETUS, "First say to yourself what you would be; and then do what you have to do"],
		[EPICTETUS, "If you want to improve, be content to be thought foolish and stupid."],
		[EPICTETUS, "Any person capable of angering you becomes your master; he can anger you only when you permit yourself to be disturbed by him"],
		[EPICTETUS, "He who laughs at himself never runs out of things to laugh at."],
		[EPICTETUS, "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control."],
		[EPICTETUS, "People are not disturbed by things, but by the views they take of them"],
		[EPICTETUS, "Circumstances don't make the man, they only reveal him to himself."],
		[EPICTETUS, "It is impossible for a man to learn what he thinks he already knows."],
		
		[BENJAMIN_FRANKLIN, "Love your Enemies, for they tell you your Faults."],
		[BENJAMIN_FRANKLIN, "No gains without pains."],
		[BENJAMIN_FRANKLIN, "He that falls in love with himself will have no rivals"],
		
	]
	
	randomQuotePair = random.choice(QUOTES_LIST)
	
	quoteFrame = FrameBuilder(AUTHORS[randomQuotePair[0]])
	
	quoteFrame.addWhitespaceLine()
	quoteFrame.addCenteredTextLine(randomQuotePair[1], amountOfExtraPadding = 4)
	quoteFrame.addWhitespaceLine()
	
	quoteFrame.printFrame()

"""
	
	Print a frame of the main commands of Apollo.
	
"""
def printCommandsFrame():
	
	commandsFrame = FrameBuilder("Apollo Commands")
	
	commandsFrame.addKeyValuePairLine("BTEST ", "Back Test Current Market Data in Real Time")
	commandsFrame.addKeyValuePairLine("INFO  ", "Get Information About Apollo")
	commandsFrame.addKeyValuePairLine("QUOTE ", "Get a Random Inspirational Quote")
	commandsFrame.addKeyValuePairLine("HELP  ", "Display These Commands")
	commandsFrame.addKeyValuePairLine("DONATE", "Donate Crypto to Pr1zmo")
	commandsFrame.addKeyValuePairLine("CREDIT", "Display Credits")
	commandsFrame.addKeyValuePairLine("CLS   ", "Clear the Terminal")
	commandsFrame.addKeyValuePairLine("EXIT  ", "Exit Apollo")
	
	commandsFrame.printFrame()

"""
	
	Print credits for Apollo.
	
	Some probably aren't needed, but are deserved.
	
"""
def printCreditsFrame():
	
	creditsFrame = FrameBuilder("CREDITS")
	
	creditsFrame.addKeyValuePairLine("PYTHON    ", "https://python.org")
	creditsFrame.addKeyValuePairLine("MATPLOTLIB", "https://matplotlib.org")
	creditsFrame.addKeyValuePairLine("COLORED   ", "https://gitlab.com/dslackw/colored")
	creditsFrame.addKeyValuePairLine("COINGECKO ", "https://coingecko.com/en/api/documentation")
	creditsFrame.addKeyValuePairLine("BIXENSE   ", "https://bixense.com/clicolors")
	creditsFrame.addKeyValuePairLine("PLTW      ", "https://pltw.org")
	
	creditsFrame.printFrame()

"""
	
	A basic class for building frames within the terminal output.
	
	Parameters:
		
		title (str) = "": A title for the frame, if wanted.
		isDoubleLine (bool): Intended to set the frame lines using the ASCII box lines. Not used yet.
		textWrap (int) = TEXT_WRAP_WORD: Mode for wrapping words that overflow the FRAME_LENGTH.
		isDelimiterDash (bool) = True: Boolean to set the delimeter for key-value pair lines. If false, use a colon (:).
	
"""
class FrameBuilder(list):
	
	TEXT_WRAP_WORD:      int = 0
	TEXT_WRAP_CHARACTER: int = 1
	TEXT_MODE_CUTTOF:    int = 2
	
	FRAME_LENGTH: int = 65
	LINE_LENGTH:  int = (FRAME_LENGTH - 4)
	
	title: str
	
	isDoubleLine: bool
	
	textWrap: int
	
	isDelimiterDash: bool
	
	def __init__(self, title: str = "", isDoubleLine: bool = True, textWrap: int = TEXT_WRAP_WORD, isDelimiterDash: bool = True):
		
		self.title = title
		
		self.isDoubleLine = isDoubleLine
		
		self.textWrap = textWrap
		
		self.isDelimiterDash = isDelimiterDash
		
		self.addFrameTop()
	
	"""
		
		Add a title to the frame. Automatically called by FrameBuilder().__init__().
		
	"""
	def addFrameTop(self):
		
		if (self.title != ""):
			
			frameFiller = ('═' * getRoundedUp((FrameBuilder.LINE_LENGTH - len(self.title)) // 2))
			
			self.append(f"{TERMINAL_THEME.frameBox}╔{frameFiller}[{TERMINAL_THEME.frameTitle}{self.title}{TERMINAL_THEME.frameBox}]{frameFiller}╗")
		
		else:
			
			self.append(f"{TERMINAL_THEME.frameBox}╔{'═' * (FrameBuilder.FRAME_LENGTH - 2)}╗")
	
	"""
		
		Automatically called by FrameBuilder().printFrame().
		
	"""
	def addFrameBottom(self):
		
		self.append(f"╚{('═' * (FrameBuilder.FRAME_LENGTH - 2))}╝")
	
	def addWhitespaceLine(self):
		
		self.append(f"║ {(' ' * FrameBuilder.LINE_LENGTH)} ║")
	
	def addTextLine(self, text: str, color: str = ""):
		
		if (color == ""):
			
			color = TERMINAL_THEME.frameText
		
		self.append(f"║ {color}{text}{(' ' * (FrameBuilder.LINE_LENGTH - len(text)))} {TERMINAL_THEME.frameBox}║")
	
	def addKeyValuePairLine(self, key: str, value: str):
		
		delimiter = (" -" if self.isDelimiterDash else ":")
		
		keyValueLength = len(f"{key}{delimiter} {value}")
		
		self.append(f"║ {TERMINAL_THEME.frameKey}{key}{TERMINAL_THEME.frameDelimiter}{delimiter} {TERMINAL_THEME.frameValue}{value}{(' ' * (self.LINE_LENGTH - keyValueLength))} {TERMINAL_THEME.frameBox}║")
	
	def addCenteredTextLine(self, text: str, amountOfExtraPadding: int = 0):
		
		textLength = len(text)
		
		totalExtraPaddingAmount = (amountOfExtraPadding * 2)
		
		if ((textLength + totalExtraPaddingAmount) > FrameBuilder.LINE_LENGTH):
			
			amountOfExcessText = (textLength - FrameBuilder.LINE_LENGTH)
			
			excessTextIndex = ((textLength - amountOfExcessText) - totalExtraPaddingAmount)
			
			currentText = text[:excessTextIndex]
			
			spacePadding = (' ' * (((FrameBuilder.LINE_LENGTH - len(currentText)) // 2)))
			
			self.append(f"║ {spacePadding}{TERMINAL_THEME.frameText}{currentText}{spacePadding} {TERMINAL_THEME.frameBox}║")
			
			self.addCenteredTextLine(text[excessTextIndex:], amountOfExtraPadding)
		
		else:
			
			spacePadding = (' ' * ((FrameBuilder.LINE_LENGTH - textLength) // 2))
			
			self.append(f"║ {spacePadding}{TERMINAL_THEME.frameText}{text}{spacePadding} {TERMINAL_THEME.frameBox}║")
	
	def printFrame(self):
		
		self.addFrameBottom()
		
		print()
		
		for line in self:
			
			println(line)
