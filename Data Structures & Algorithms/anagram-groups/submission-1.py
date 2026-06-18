class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createDict(string):
            newDict = {}
            for char in string:
                if char in newDict:
                    newDict[char] +=1
                else: newDict[char] = 1
            return newDict
        
        dictionaries = []
        result = []
        for string in strs:
            thisDict = createDict(string)
            if thisDict in dictionaries:
                result[dictionaries.index(thisDict)].append(string)
            else:
                result.append([string])
                dictionaries.append(thisDict)
        return result