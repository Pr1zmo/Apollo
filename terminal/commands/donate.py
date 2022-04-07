from terminal.print import FrameBuilder

"""
	
	Command for displaying cryptocurrency addresses of the developer.
	
"""
def executeCommandDonate():
	
	donateFrame = FrameBuilder("Donate Crypto", isDelimiterDash = False)
	
	donateFrame.addKeyValuePairLine("Bitcoin (BTC)", "39ha5tizVMYMSTYqPFdmKUvBnVK26MKnDC")
	donateFrame.addWhitespaceLine()
	
	donateFrame.addKeyValuePairLine("Ethereum (ETH)", "0x37CE3AB0cf1584139425c8Eb06dc8296Ff12Fc63")
	donateFrame.addWhitespaceLine()
	
	donateFrame.addKeyValuePairLine("Tezos (XTZ)", "tz1M7GrL8Rs5P1kM9CtRHjNwLs5gqyiswazv")
	donateFrame.addWhitespaceLine()
	
	donateFrame.printFrame()