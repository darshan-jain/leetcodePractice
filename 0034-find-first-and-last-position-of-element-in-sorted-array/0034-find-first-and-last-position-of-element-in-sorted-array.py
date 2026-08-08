#import bisect - gives the insertion index to which the number needs to be added
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        def search(isFirst):
            first = -1
            l = 0 
            r = len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m] == target:
                    if isFirst:
                        first = m
                        r = m-1
                    else:
                        first = m
                        l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return first
        
        res[0] = search(True)
        res[1] = search(False)
        return res
                 


        
        