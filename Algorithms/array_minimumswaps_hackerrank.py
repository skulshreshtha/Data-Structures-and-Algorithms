#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0       # Initialize the swaps count
	index_dict = {v:i for i,v in enumerate(arr)}		# Store the index for each item for O(1) access
	
	for i,v in enumerate(arr):
		if(v != i+1):
			to_idx = index_dict.get(i+1)				# Find out where the element for this position is
			arr[i], arr[to_idx] = arr[to_idx], arr[i]	# Swap values
			index_dict[i+1] = i							# Fixing the dictionary
			index_dict[v] = to_idx
			swaps += 1
	return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
