class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = float("-inf")

        for i, colori in enumerate(colors):
            for j, colorj in enumerate(colors):
                if i!=j and colori!=colorj:
                    res = max(res, abs(i-j))
        return res
                    