class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        letters = ['a','b','c']

        def backtrack(path):
            if len(path)==n:
                res.append("".join(path[:]))
                return 
            for i in range(len(letters)):
                if letters[i]!=path[-1]:
                    path.append(letters[i])
                    backtrack(path)
                    path.pop()


        for i in range(len(letters)):
            backtrack([letters[i]])
        if k > len(res):
            return ""
        return res[k-1]
        