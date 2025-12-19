class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letterset = []
        for i in range(len(s)):
            if s[i].isalpha():
                letterset.append(i)
        res = []
        def recr(parstr, idx):
            if idx==len(letterset):
                res.append(parstr)
                return 
            if idx > len(letterset):
                return 
            cap = parstr[0:letterset[idx]] + parstr[letterset[idx]].upper() + parstr[letterset[idx]+1:]
            nocap = parstr[0:letterset[idx]] + parstr[letterset[idx]].lower() + parstr[letterset[idx]+1:]
            recr(cap, idx+1)
            recr(nocap, idx+1)
        if letterset:  
            recr(s,0)
        else:
            return [s]
        return res
        