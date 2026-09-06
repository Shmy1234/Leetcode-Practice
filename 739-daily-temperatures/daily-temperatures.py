class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                s_i = stack.pop()[1]
                res[s_i] = i - s_i
            stack.append((t, i))
        
        return res
        