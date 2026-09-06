class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m = 0
        while j < len(prices):
            while prices[i] > prices[j]:
                i+=1 
            m = max(m, prices[j] - prices[i])
            j+=1 
        return m