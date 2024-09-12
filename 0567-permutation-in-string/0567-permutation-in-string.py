class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, window = {}, {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1
        matches = 0
        for c in s1Count:
            if s1Count[c] == window.get(c, 0):
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1Count):
                return True
            c = s2[r]
            window[c] = window.get(c, 0) + 1
            if c in s1Count and window[c] == s1Count[c]:
                matches += 1
            elif c in s1Count and window[c] == s1Count[c] + 1:
                matches -= 1
            
            c = s2[l]
            window[c] = window.get(c, 0) - 1
            if c in s1Count and window[c] == s1Count[c]:
                matches += 1
            elif c in s1Count and window[c] == s1Count[c] - 1:
                matches -= 1
            
            l += 1
        return matches == len(s1Count)