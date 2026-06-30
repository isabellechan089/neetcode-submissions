class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        i, j = 0,0
        maxchar = 0
        maxlen = 0
        while j < len(s):
            if s[j] in counts:
                counts[s[j]] +=1
            else:
                counts[s[j]] = 1
            maxchar = max(counts[s[j]], maxchar)
            if (j-i+1 - maxchar) <= k:
                maxlen = max(j-i+1, maxlen)
                j+=1
            else:
                counts[s[i]] -=1
                i+=1
        return maxlen