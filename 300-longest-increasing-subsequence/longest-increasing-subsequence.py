class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = [nums[0]]
        max_len = 1
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
                max_len+=1
            else:
                # ind =0 
                # while ind < len(lst) and lst[ind] < num:
                #     ind+=1
                # lst[ind] = num
                left, right = 0,len(lst)-1
                while left < right:
                    mid = (left+right)//2
                    if lst[mid] < num : 
                        left = mid +1
                    else:
                        right = mid
                lst[left] = num


        return max_len

        #can be optimised for else part using binary search

        