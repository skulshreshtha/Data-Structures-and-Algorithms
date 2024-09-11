class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        start = 0
        maxLength = 0
        for i, c in enumerate(s):
            if c in lastSeen:
                start = max(lastSeen[c] + 1, start)
            maxLength = max(maxLength, i - start + 1)
            lastSeen[c] = i
        return maxLength