"""
	
	Get a number rounded up. Due to the fact that in Python, a literal True correlates with the integer 1,
	and the literal False correlates with the integer 2, if you were to cast a float to an integer, then you can 
	just check if the number has a remainder when dividing by 1, (decimals can't divide by one), and add 1 to
	the int of the float.
	
	Ex. 1: getRoundedUp(5.2):
		
		Int cast of 5.2 == 5.
		(5.2 / 1) has remainder of .2, so add True (1).
		5 + 1 = 6.
		return 6.
	
	Ex. 2: getRoundedUp(5)
		
		Int cast of 5 == 5.
		(5 / 1) has remainder of 0, so add False (0).
		5 + 0 = 5.
		Return 5.
	
	Parameters:
		
		number: A number.
	
	Returns:
		
		int: The integer of the number rounded up.
	
"""
def getRoundedUp(number) -> int:
	
	# True  == 1
	# False == 0
	
	return (int(number) + (number % 1 > 0))

"""
	
	Get the percentage of a number of another number.
	
	Parameters:
		
		integer_1 (int): A valid integer.
		integer_2 (int): A valid integer.
	
	Returns:
		
		float: A percentage in base 10 of the given numbers.
	
"""
def getPercentage(integer_1: int, integer_2: int) -> float:
	
	return ((integer_1 / integer_2) * 100)