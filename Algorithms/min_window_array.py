class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        d = Counter(t)
        count = len(d)      # Number of unique chars in dictionary
        i = j = 0
        min_window = float(inf)      # Initializing to largest window possible
        min_word = ""
        
        while (j < n):
            
            # Increasing j and reducing dict count each time we find a pattern character
            while(count > 0 and j < n):
                if(s[j] in d):
                    d[s[j]] -= 1
                    if(d[s[j]] == 0):
                        count -= 1      # Found enough of one unique character
                j += 1
            
            # Reducing left wall to optimize what we found
            while (i<=j and count == 0):
                if(min_window > j-i):
                    min_window = j-i   # Update window size
                    min_word = s[i:j]                   # Update word
                
                if(s[i] in d):
                    d[s[i]] += 1
                    if(d[s[i]] > 0):
                        count += 1                  # need more of this character
                i += 1
                
        
        return min_word