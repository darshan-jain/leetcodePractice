class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        num_set = set(nums)
        maxLen = 1
        for num in num_set:
            curNum = num
            curLength = 1
            if curNum-1 not in num_set:
                while curNum+1 in num_set:
                    curNum= curNum+1
                    curLength +=1
                    maxLen = max(maxLen, curLength)
        
        return maxLen
        