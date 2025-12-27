class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, m = 0, 0, 0
        while j < len(prices):
            if i == j:
                j += 1
            elif prices[i] > prices[j]:
                i += 1
            else:
                m = max(m, prices[j] - prices[i])
                j += 1
        return m
        