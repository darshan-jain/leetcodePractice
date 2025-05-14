class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = set(nums1)
        arr2 = set(nums2)
        res = []
        val = []
        for num in arr1:
            if num not in arr2:
                val.append(num)
        
        res.append(val)
        val = []
        for num in arr2:
            if num not in arr1:
                val.append(num)
        res.append(val)
        return res

        