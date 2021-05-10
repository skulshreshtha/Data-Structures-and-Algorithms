import Empty

class ArrayQueue:
	""" FIFO implementation of abstract data type queue using Python list as underlying storage."""
	DEFAULT_CAPACITY = 10		# Initial capacity for all new queues
	
	def __init__(self):
		""" Create an empty queue."""
		self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0
		
	def __len__(self):
		""" Return size of the queue. """
		return self._size
		
	def is_empty(self):
		""" Return True if the queue is empty, False otherwise."""
		return self._size == 0
	
	def first(self):
		""" Return (but not remove) the first element in the queue. Raise error is queue is empty."""
		if (self.is_empty()):
			raise Empty('Queue is empty.')
		return self._data[self._front]
	
	def dequeue(self):
		""" Return and remove the first element in the queue. Raise error if queue is empty."""
		if (self.is_empty()):
			raise Empty('Queue is empty.')
		answer = self._data[self._front] 		# Front element to be returned
		self._data[self._front] = None			# Garbage collection
		self._front = (self._front + 1) % len(self._data) 		# Using modulus to create circular effect
		self._size -= 1							# Reduce size of queue
		
		if (0 < self._size <= len(self._data) // 4):	# If queue occupying less than 25% of list space
			self._resize(len(self._data)//2)		# Halve the list length
		return answer
		
	def enqueue(self, e):
		""" Add an element e to the back of the queue."""
		if (self._size == len(self._data)):		# Array is fully used
			self.resize(2 * len(self._data))	# Double the array size
		store_idx = (self._front + self._size) % len(self._data)
		self._data[store_idx] = e
		self._size += 1 						# Increasing size
		
	def _resize(self, cap):
		""" Resize the underlying list to new size."""
		old = self._data			# Store the old data
		self._data = [None] * cap	# Create a blank new list
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[(self._front + k) % len(old)] # Bring elements in order from old list
		self._front = 0 			# Realign the front
		