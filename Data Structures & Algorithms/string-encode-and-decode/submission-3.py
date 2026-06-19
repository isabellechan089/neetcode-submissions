class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string + "é"
        return result[:-1]
    def decode(self, s: str) -> List[str]:
        return s.split("é")