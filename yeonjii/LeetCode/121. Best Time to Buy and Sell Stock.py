import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = sys.maxsize
        for price in prices:
            ans = max(ans, price-min_val)
            if price < min_val:
                min_val = price
        return ans