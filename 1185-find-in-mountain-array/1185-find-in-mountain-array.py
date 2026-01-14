# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #find peak index 
        l = 0 
        r= mountainArr.length()-1
        while l<r:
            m = (l+r)//2
            if mountainArr.get(m)<mountainArr.get(m+1):
                l = m+1
            else:
                r = m-1
        
        if mountainArr.length()%2==0:
            r+=1
        #BS on left 
        low = 0 
        high = r 
        while low<=high:
            m = (low+high)//2
            val = mountainArr.get(m)
            if val==target:
                return m
            elif val > target:
                high = m-1
            else:
                low = m+1

        #BS on right
        low = r
        high = mountainArr.length()-1
        while low<=high:
            m = (low+high)//2
            val = mountainArr.get(m)
            if val==target:
                return m
            elif val > target:
                low = m+1
            else:
                high= m-1
        return -1

        