class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        # [(0,2)]
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = (i - index)
                maxArea = max(maxArea, width * height) # 2
                start = index
            stack.append((start, h)) # Backwards extend rectangle of current height
        
        while stack:
            index, height = stack.pop()
            width = (len(heights) - index)
            maxArea = max(maxArea, width * height)

        return maxArea