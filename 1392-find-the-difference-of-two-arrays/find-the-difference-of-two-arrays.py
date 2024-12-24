class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res = []
        answer1 = []
        answer2 = []

        for num in nums1:
            if num not in nums2 and num not in answer1:
                answer1.append(num)
        
        for num in nums2:
            if num not in nums1 and num not in answer2:
                answer2.append(num)
        res = [answer1, answer2]

        return res
        