class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {}
        def helper(am):
            if am == 0: return 0
            if am < 0: return float('inf')
            if am in seen: return seen[am]

            min_coins = float('inf')
            # Test EVERY coin option at this current amount
            for c in coins:
                res = helper(am - c)
                # Keep track of the best outcome
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            seen[am] = min_coins
            return seen[am]

        ans = helper(amount)
        return ans if ans != float('inf') else -1