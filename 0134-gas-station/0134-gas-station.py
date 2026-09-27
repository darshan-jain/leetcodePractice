class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        index = 0 
        tot = 0 
        for i in range(len(gas)):
            tot += gas[i]-cost[i]
            if tot<0:
                tot=0
                index=i+1
        
        return index

            
        