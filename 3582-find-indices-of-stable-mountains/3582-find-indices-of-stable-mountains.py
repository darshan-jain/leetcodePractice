class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for i in range(len(height)):
            if i>0 and height[i-1]>threshold:
                res.append(i)
        return res
        