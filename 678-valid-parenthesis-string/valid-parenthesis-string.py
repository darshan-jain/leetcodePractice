class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min =0 
        max =0 
        for i in range(len(s)):
            if s[i] == '(':
                min = min+1
                max = max+1
            elif s[i] == ')':
                min = min-1
                max = max-1
            else:
                min = min-1
                max = max+1
            if min <0:
                min=0
            if max <0:
                return False
        return min==0
        