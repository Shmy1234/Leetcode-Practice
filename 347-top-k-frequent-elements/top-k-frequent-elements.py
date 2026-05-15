class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums: 
            d[n] = d.get(n, 0) + 1
        l = []
        
        for key, val in d.items():
            l.append((val, key))

        l.sort()
        res = []

        for i in range(k):
            res.append(l.pop()[1])
        return res