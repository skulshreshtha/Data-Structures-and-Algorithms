class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        tCount, window = {}, {}
        have, need = 0, 0
        minwindow, minLength = "", float("inf")
        for i in range(len(t)):
            if t[i] not in tCount:
                need += 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        l = 0
        for r in range(len(s)):
            if s[r] in tCount:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == tCount[s[r]]:
                    have += 1
                while have == need:
                    if r - l + 1 < minLength:
                        minwindow = s[l:r+1]
                        minLength = r - l + 1
                    if s[l] in window:
                        window[s[l]] -= 1
                        if window[s[l]] < tCount[s[l]]:
                            have -= 1
                    l += 1
        return minwindow