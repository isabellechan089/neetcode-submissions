class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = {}
        top = -float('inf')
        for num in nums:
            if num in freq:
                freq[num] +=1
            else: freq[num] = 1
        for key, v in freq.items():
            if v >= top:
                result.append(key)
                if len(result) >k:
                    del result[0]
        return result      