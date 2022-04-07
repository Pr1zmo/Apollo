import colored

from terminal.utilities import ANSI_COLORS_ENABLED

"""
	
	Get the ANSI foreground escape sequence for a color, if enabled.
	
	Parameters:
		
		color (str): A color. This is can either be a literal name, such as red, or a hex value prepended with #.
	
	Returns:
		
		str: An ANSI escape sequence for the foreground color, if enabled, of the supplied color value.
	
"""
def fg(color: str) -> str:
	
	return (colored.fg(color) if ANSI_COLORS_ENABLED else "")

"""
	
	A configuration class meant to be used by various print functions for displaying
	colors within a terminal that supports ANSI escape sequences.
	
"""
class TerminalTheme():
	
	banner:         str
	frameBox:       str
	frameTitle:     str
	frameKey:       str
	frameDelimiter: str
	frameValue:     str
	frameText:      str
	commandInput:   str
	
	def __init__(self, theme: str):
		
		if (not ANSI_COLORS_ENABLED):
			
			self.banner         = ""
			self.frameBox       = ""
			self.frameTitle     = ""
			self.frameKey       = ""
			self.frameDelimiter = ""
			self.frameValue     = ""
			self.frameText      = ""
			self.commandInput   = ""
			
			return
		
		# * Order: Banner, Frame Box, Frame Title, Frame Key, Frame Delimiter, Frame Value, Frame Text, Command Input
		
		THEME_MAP = {
			
			"mana": [fg(165), "\33[1;35m", fg("#87FF87"), fg("#FF9AC1"), "\33[1;32m", "\33[38;5;93m", fg("#FF2C6D"), "\33[1;36m"]
			
		}
		
		correctTheme = THEME_MAP.get(theme.lower())
		
		self.banner         = correctTheme[0]
		self.frameBox       = correctTheme[1]
		self.frameTitle     = correctTheme[2]
		self.frameKey       = correctTheme[3]
		self.frameDelimiter = correctTheme[4]
		self.frameValue     = correctTheme[5]
		self.frameText      = correctTheme[6]
		self.commandInput   = correctTheme[7]