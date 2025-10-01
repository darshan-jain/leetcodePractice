class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)):
            if i>=2:
                cost[i] = cost[i] +  min(cost[i-1],cost[i-2])
        return cost[-1] if cost[-1] < cost[-2] else cost[-2]

        