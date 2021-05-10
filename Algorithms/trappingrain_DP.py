class Solution:
    
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        n = len(height)
        left = [0]*n
        right = [0]*n
        
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1,n):
            left[i] = max(left[i-1],height[i])
            right[n-1-i] = max(right[n-i],height[n-1-i])
        
        water = 0
        for i in range(n):
            water += min(left[i],right[i]) - height[i]
        
        return water