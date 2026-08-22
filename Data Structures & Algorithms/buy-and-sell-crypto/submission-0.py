class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        diff = 0
        for i in prices:
            if i <= min_val:
                min_val = i
            if abs(min_val - i) >= diff:
                diff = abs(min_val - i)
        return diff
