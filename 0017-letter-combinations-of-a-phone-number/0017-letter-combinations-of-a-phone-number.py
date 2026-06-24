class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digittostr = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        def dfs(idx,curr):
            if idx==len(digits):
                res.append(curr)
                return 
            for j in digittostr[digits[idx]]:
                dfs(idx+1,curr+j)

        dfs(0,"")
        return res

       