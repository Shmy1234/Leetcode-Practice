class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        l2 = []
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for k2,v in d.items():
            l.append((v,k2))
        l.sort()
        for i in range(k):
            l2.append(l.pop()[1])
        return l2  