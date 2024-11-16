class Solution(object):
    # def helper(self,n):
    #     count =0
    #     while n:
    #         n = n&(n-1)
    #         count+=1
    #     return count
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # res = []
        # for i in range(n+1):
        #     ot = self.helper(i)
        #     res.append(ot)
        # return res
        res = [0]
        for i in range(1,n+1):
            res.append(res[i//2]+i%2)
        return res