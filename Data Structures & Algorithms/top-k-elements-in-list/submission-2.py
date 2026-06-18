class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = {}
        top = -float('inf')
        for num in nums:
            if num in freq:
                freq[num] +=1
            else: freq[num] = 1
        top_k_keys = sorted(freq, key=freq.get, reverse=True)[:k]
        return top_k_keys