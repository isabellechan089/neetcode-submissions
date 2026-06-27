class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = 0
        j = len(s1) -1
        s1frq = {}
        for char in s1:
            s1frq[char] = 1 + s1frq.get(char, 0)
        s2frq = {}
        for idx in range(len(s1)):
            char = s2[idx]
            s2frq[char] = 1+s2frq.get(char, 0)

        while j < len(s2):
            if s1frq == s2frq:
                return True
            s2frq[s2[i]]-=1
            if s2frq[s2[i]] == 0:
                del s2frq[s2[i]]
            i+=1
            j+=1
            if j < len(s2):
                s2frq[s2[j]] = 1+s2frq.get(s2[j],0)
        return False