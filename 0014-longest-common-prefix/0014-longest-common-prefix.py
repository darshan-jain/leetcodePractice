class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        shortest = min(strs,key=len)
        for j in range(len(shortest)):
            for i in range(len(strs)):
                if strs[i][j]!=shortest[j]:
                    return ans
            ans+=shortest[j]
        return ans
        