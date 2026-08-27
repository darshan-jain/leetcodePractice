class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hm = defaultdict(list)


        def getdist(v):
            return abs(v[0]-v[1]) + abs(v[1]-v[2]) + abs(v[2]-v[0])

        for i, num in enumerate(nums):
            hm[num].append(i)
        res = float("inf")
        for k,v in hm.items():
            if len(v)>=3:
                for i in range(len(v)-3+1):
                    dist = getdist(v[i:i+3])
                    res = min(res, dist)
        return res if res!=float("inf") else -1
        