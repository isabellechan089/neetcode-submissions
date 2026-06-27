class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minlen = float('inf')
        if len(t) > len(s):
            return res
        tdic = {}
        for char in t:
            tdic[char] = 1+tdic.get(char,0)
        need = len(tdic)
        have = 0
        i=0
        sdic = {}
        for j in range(len(s)):
            sdic[s[j]] = 1+sdic.get(s[j], 0)
            if sdic[s[j]] == tdic.get(s[j]):
                have+=1
            while need == have:
                
                cur = s[i:j+1]
                if len(cur) < minlen:
                    res = cur
                minlen = min(minlen, len(cur))
                char = s[i]
                sdic[char] -=1
                if char in tdic and sdic[char] < tdic[char]:
                    have -= 1
                i+=1

        return res
            