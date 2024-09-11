"""
AABABBA
l, maxLength, curLenght, counter, candidates
0,1,1,{A:1},{A}
0,2,2,{A:2},{A}
0,3,3,{A:3},{A}
0,
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxLength = 0, 0
        counter = collections.defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            curLength = r - l + 1
            maxf = max(maxf, counter[s[r]])
            # We need at least one character which has curLength-k occurences
            if curLength - maxf <= k:
                maxLength = max(maxLength, curLength)
            else:
                counter[s[l]] -= 1
                l += 1
        return maxLength