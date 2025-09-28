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
        def backtrack(index, curStr):
            if index==len(digits):
                res.append(curStr[:])
                return 
            for j in digittostr[digits[index]]:
                backtrack(index+1, curStr + j)


        if digits:
            backtrack(0,"")
        return res
        