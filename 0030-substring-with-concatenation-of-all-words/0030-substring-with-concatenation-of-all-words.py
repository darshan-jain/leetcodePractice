from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        k = len(words[0])
        numWords = len(words)
        totalLen = k * numWords
        wordCount = Counter(words)
        res = []
        
        for i in range(k):
            left = i
            subCount = Counter()
            count = 0
            
            for j in range(i, len(s) - k + 1, k):
                word = s[j:j + k]
                if word in wordCount:
                    subCount[word] += 1
                    count += 1
                    
                    while subCount[word] > wordCount[word]:
                        leftWord = s[left:left + k]
                        subCount[leftWord] -= 1
                        count -= 1
                        left += k
                        
                    if count == numWords:
                        res.append(left)
                else:
                    subCount.clear()
                    count = 0
                    left = j + k
                    
        return res