from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False 
        
        count = Counter(nums)
        sorted_keys = sorted(count.keys())

        for num in sorted_keys:
            freq = count[num]
            if freq>0:
                for i in range(k):
                    if count[num+i] < freq:
                        return False 
                    count[num+i]-=freq
        return True
        