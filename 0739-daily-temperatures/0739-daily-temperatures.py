"""
Index of the first number greater than the current number on right side
[73,74,72,74,75] -> [1,3,1,1,0]
[30,31,32,33,34] -> [1,1,1,1,0]
[75,72,73,74,76] -> [4,1,1,1,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)
        # minIndexWithoutAns = 0
        # for i in range(len(temperatures)):
        #     for j in range(i-1,minIndexWithoutAns-1,-1):
        #         if temperatures[i] > temperatures[j] and ans[j] == 0:
        #             ans[j] = i - j
        #             minIndexWithoutAns = min(j, minIndexWithoutAns)
        # return ans
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
                
