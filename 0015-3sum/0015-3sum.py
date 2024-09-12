"""
[-1,-1,0,1,2,4]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum < 0:
                    j += 1
                elif curSum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res
