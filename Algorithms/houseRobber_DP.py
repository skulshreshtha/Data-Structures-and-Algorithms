from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Define the base cases
        m = defaultdict(int)
        m[0] = nums[0]
        m[1] = max(nums[0:2])
        
        for i in range(2,len(nums)):
            m[i] = max(m[i-1], nums[i] + m[i-2])
        
        return m[len(nums)-1]