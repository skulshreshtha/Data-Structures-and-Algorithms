class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        res = [[]]
        for x in nums:
            for ele in res:
                res = res + ([ele + [x]])
        
        return res