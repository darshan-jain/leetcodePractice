class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(o,c,s):
            if o==0 and c==0:
                res.append(s)
                return 
            if o>0:
                backtrack(o-1,c,s+'(')
            if c>o:
                backtrack(o,c-1,s+')')
            

        backtrack(n,n,"") #number of open, number of close
        return res
        