# Program to match parenthesis using Stack

import ArrayStack

def is_matched(expr):
	""" Return True if the parenthesis match, else return False. """
	
	lefty = "[{("		# Opening delimiters
	righty = "]})"		# Closing delimiters
	
	S = ArrayStack()	# Initialize empty stack
	
	for c in expr:
		if (c in lefty): 
			S.push(c)	# Push left delimiter into stack
		elif (c in righty):
			if (S.is_empty()):
				return False		# No matching opening delimiter
			if (righty.index(c) != lefty.index(S.pop())):
				return False 		# Delimiters do not match
	
	return S.is_empty()		# All matched if stack is empty at end
	