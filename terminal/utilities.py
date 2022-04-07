import os
import sys

from subprocess import run

ANSI_COLORS_ENABLED = False

"""
	
	Clear the screen of terminal. Compatible with Windows and UNIX systems.
	
"""
def clearTerminalScreen():
	
	# * nt == Windows New Technology
	
	if (os.name == "nt"):
		
		run("cls", shell = True)
	
	else:
		
		run("clear", shell = True)

"""
	
	Set the size of terminal. Only compatible with Windows systems.
	
"""
def setTerminalSize():
	
	if (os.name == "nt"):
		
		run(["mode", "con:", "cols=69", "lines=40"], shell = True)

"""
	
	Check if ANSI color sequencing is available by either checking for common
	environment variables, or prompting the user by asking them if an output 
	is correctly displayed.
	
"""
def isANSIColorsEnabled():
	
	if (sys.stdout.isatty()):
		
		global ANSI_COLORS_ENABLED
		
		# * Environment Variables are From: https://bixense.com/clicolors
		
		if (("ANSICON" in os.environ) or (os.getenv("CLICOLOR", "0") != "0") or (os.getenv("CLICOLOR_FORCE", "0") == "1")):
			
			ANSI_COLORS_ENABLED = True
			
		else:
			
			clearTerminalScreen()
			
			# * Reset Terminal Attributes, and Set Foreground Text Color to Purple
			
			print("\33[0m\33[1;35m")
			
			inputColorAnswer = input("Is This Text Pink/Purple? (Y/N): ")
			
			ANSI_COLORS_ENABLED = ((inputColorAnswer == "y") or (inputColorAnswer == "yes"))