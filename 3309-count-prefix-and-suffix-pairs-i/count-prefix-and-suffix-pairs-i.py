class Solution:
    def isPrefixAndSuffix(self,str1,str2):
        
        if len(str1) > len(str2):
            return False
        elif str2[0:len(str1)] == str1 and str2[len(str2) - len(str1):len(str2)] == str1:
            return True
        else:
            return False
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0 
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]) == True:
                    ans+=1
        
        return ans
        