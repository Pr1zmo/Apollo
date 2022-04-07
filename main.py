import time

from terminal.utilities import isANSIColorsEnabled, clearTerminalScreen, setTerminalSize

# * Check if ANSI Color Sequences are Enabled

clearTerminalScreen()

isANSIColorsEnabled()

from terminal.print           import TERMINAL_THEME, printMainMenu, printInfoFrame, printQuoteFrame, printCommandsFrame, printCreditsFrame
from terminal.commands.btest  import executeCommandBTest
from terminal.commands.donate import executeCommandDonate
from terminal.input           import CommandsManager, getInput
from terminal.theme           import fg

"""
	
	Clear the terminal and print the main menu.
	
"""
def executeClearScreen():
    
	setTerminalSize()
	
	clearTerminalScreen()
	
	printMainMenu()

"""
	
	The main method, and starting point for the program.
	
"""
def main():
	
	executeClearScreen()
	
	commandsManager = CommandsManager()
	
	commandsManager.addCommands(executeCommandBTest,  "btest", "backtest")
	commandsManager.addCommands(printInfoFrame,       "info", "about")
	commandsManager.addCommands(printQuoteFrame,      "quote")
	commandsManager.addCommands(printCommandsFrame,   "help", "?")
	commandsManager.addCommands(executeCommandDonate, "donate")
	commandsManager.addCommands(printCreditsFrame,    "credit", "credits")
	commandsManager.addCommands(executeClearScreen,   "cls", "clear", "restart", "reset")
	commandsManager.addCommands(exit,                 "exit", "quit")
	
	while True:
		
		try:
			
			print(f"\n  {TERMINAL_THEME.frameBox}┌─────[{TERMINAL_THEME.frameKey}root{TERMINAL_THEME.frameDelimiter}@{TERMINAL_THEME.frameValue}Apollo{TERMINAL_THEME.frameBox}]───[{fg('cornflower_blue')}{time.strftime('%I:%M:%S %p')}{TERMINAL_THEME.frameBox}]")
			inputCommand = getInput(f"└──────> {fg(122)}# {TERMINAL_THEME.commandInput}")
			
			if (inputCommand != ""):
				
				commandsManager.executeCommand(inputCommand.lower())
		
		except KeyboardInterrupt:
			
			executeClearScreen()
			
			continue
		
		except EOFError:
			
			continue
		
		# * Used for Debugging
		
		except Exception as exception:
			
			print(exception)

# * Prevent any Imports of main.py from Accidentally Running main() Again

if __name__ == "__main__":
    
    main()