class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        length = ""
        result = []
        check = True
        index = 0
        while index < len(s):
            char = s[index]
            if char != '#' and char.isdigit():
                length += char
                index +=1
            else:
                check = False
                wordlen = int(length)
                result.append(s[index + 1:index+wordlen + 1])
                index += wordlen + 1
        return result


