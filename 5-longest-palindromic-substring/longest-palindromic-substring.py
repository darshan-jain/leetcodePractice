class Solution(object):
    def isPal(self,string,left,right):
        while left > 0 and right <len(string)-1 and string[left-1] == string[right+1]:
            left-=1
            right+=1
        return left,right,right-left+1
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left,right,max_len = 0,0,0
        for ind in range(len(s)-1):
            l1,r1,max_len1 = self.isPal(s,ind,ind)
            if max_len1 > max_len:
                max_len = max_len1
                left,right = l1,r1
            
            if s[ind] == s[ind+1]:
                l2,r2,max_len2 = self.isPal(s,ind,ind+1)
                if max_len2> max_len:
                    max_len = max_len2
                    left,right = l2,r2
        return s[left:right+1]
        