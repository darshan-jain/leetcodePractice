"""
[1,2,3,1,2,3], k = 2
        l   i
set = [1,2]

if nums[i] in set:
    return True
else:
    add it to the set and remove nums[l] from set
 0,1,2,3
[1,2,3,1], k = 3
 l   r

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0 
        q = set()
        for r in range(len(nums)):
            if r-l > k:
                q.remove(nums[l])
                l+=1
            if nums[r] in q:
                return True
            q.add(nums[r])
        return False
            

        