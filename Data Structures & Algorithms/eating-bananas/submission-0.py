import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        lowest = upper
        while lower <= upper:
            total = 0
            mid = (lower+upper) // 2

            for p in piles:
                total+= math.ceil(p/mid)
            
            if total <=h:
                lowest = mid
                upper = mid -1
            else:
                lower = mid +1
        return lowest
