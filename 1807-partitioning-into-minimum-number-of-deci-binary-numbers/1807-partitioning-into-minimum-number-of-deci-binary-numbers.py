class Solution:
    def minPartitions(self, n: str) -> int:
        maxnum = 0 
        for c in n:
            valint = ord(c) - ord("0")
            maxnum = max(maxnum, valint)
        return maxnum
        