class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        i, j = 0,0
        chars = set()
        while j < len(s):
            if s[j] in chars:
                chars.discard(s[i])
                i +=1
            else:
                chars.add(s[j])
                j+=1
                
            length = max(j-i+1, length)
        return length -1