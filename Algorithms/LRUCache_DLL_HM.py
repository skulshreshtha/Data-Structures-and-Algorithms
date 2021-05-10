class LRUCache:
    
    class _Node:
        
        def __init__(self, key: int, val: int):
            self._key = key
            self._val = val
            self._prev = None
            self._next = None
        
        def __del__(self):
            self._key = self._val = self._prev = self._next = None # Help GC

    def __init__(self, capacity: int):
        assert capacity > 0, "Capacity should be positive"
        assert isinstance(capacity, int), "Capacity should be an integer value"
        
        # Initialize empty dictionary to store
        # key(int) -> Node(val, key)
        self._capacity = capacity
        self._m = {}
        self._size = 0
        
        # Initialize dummy header and trailer nodes
        self._dummy_head = self._Node(-1, -1)
        self._dummy_tail = self._Node(-1, -1)
        # Link the nodes
        self._dummy_head._next = self._dummy_tail
        self._dummy_tail._prev = self._dummy_head

    def get(self, key: int) -> int:
        """Return the value store for provided key. Return -1 if key not found"""
        if key not in self._m:
            return -1
        else:
            node = self._m.get(key)
            val = node._val
            self._move_to_head(node)
            return val
    
    def _move_to_head(self, node):
        """Move a certain node to front of the list"""
        # By pass the node
        node._prev._next = node._next
        node._next._prev = node._prev
        
        # Insert between dummy head and next element
        node._prev = self._dummy_head
        node._next = self._dummy_head._next
        node._next._prev = node
        node._prev._next = node
        
        
    def _remove_node(self, node):
        """Delete the node from list"""
        # By pass the node
        node._prev._next = node._next       
        node._next._prev = node._prev
        # Delete the key from dict
        del self._m[node._key]
        # Delete the node
        del node
        self._size -= 1
        
    def _add_to_front(self, node):
        """Add the given node to front of list"""
        # Insert between dummy head and next element
        node._prev = self._dummy_head
        node._next = self._dummy_head._next
        node._next._prev = node
        node._prev._next = node
        self._size += 1
        

    def put(self, key: int, value: int) -> None:
        """Put a new key value pair in our dictionary"""
        if key not in self._m:
            new_node = self._Node(key, value)
            self._m[key] = new_node     # Add to dictionary
            
            # Check if we need to remove a node
            if(self._size == self._capacity):
                self._remove_node(self._dummy_tail._prev)
            
            # Put new node at front of the list
            self._add_to_front(new_node)
            
        else:
            node = self._m.get(key)
            node._val = value             # Update the value
            self._move_to_head(node)      # Move to front