class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                curArea = height * width
                maxArea = max(curArea, maxArea)
                start = index
            stack.append((start, h)) # Because the current height can also be extended backwards
            
        # If stack not empty
        while stack:
            index, height = stack.pop()
            curArea = (len(heights) - index) * height
            maxArea = max(maxArea, curArea)
        
        return maxArea