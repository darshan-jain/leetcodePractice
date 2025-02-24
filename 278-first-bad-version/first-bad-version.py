# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        beg = 1
        end = n 
        count = 0 
        while beg <end:
            mid = (beg+end)//2
            count+=1
            if not isBadVersion(mid):
                beg = mid+1
            else:
                end = mid
        return beg


        