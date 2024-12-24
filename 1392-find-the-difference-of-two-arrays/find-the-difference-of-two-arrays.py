class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for num in nums1:
            if num not in nums2 :
                ans.append(num)

        res.append(ans)
        ans = []
        
        for num in nums2:
            if num not in nums1 :
                ans.append(num)
        res.append(ans)

        return res
        