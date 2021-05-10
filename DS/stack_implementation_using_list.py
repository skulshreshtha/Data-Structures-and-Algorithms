class Empty(Exception):
	""" Error in attempting to access element from an empty container."""
	pass

class ArrayStack:
	""" LIFO implementation of the abstract data type Stack using Python list as underlying storage. """
	
	def __init__(self):
		""" Create an empty stack. """
		self._data = []		# protected list instance
		
	
	def __len__(self):
		""" Getting the number of elements in stack."""
		return len(self._data)
		
	def is_empty(self):
		""" Return True if the stack is empty."""
		return len(self._data) == 0
		
	def push(self, e):
		""" Add element e to top of the Stack."""
		self._data.append(e)		# New element added to end of the list
		
	def top(self):
		""" Return reference to the top element without removing it from the Stack. Raise error if stack is empty."""
		if(self.is_empty()):
			raise Empty("Stack is empty.")
		return self._data[-1] 		# Return the last item in list
		
	def pop(self):
		""" Return and remove the top element from the stack. Raise error if stack is empty. """
		if(self.is_empty()):
			raise Empty("Stack is empty.")
		return self._data.pop()		# Remove the last element from list