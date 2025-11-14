class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        totwords = len(words)
        wordsize = len(words[0])
        winsize = totwords * wordsize
        freq_count = Counter(words)
        res = []

        for i in range(len(s)- winsize+1):
            curr_freq = {}
            j = i 
            while j< i + winsize:
                curr_word = s[j:j+wordsize]
                if curr_word not in freq_count:
                    break
                curr_freq[curr_word] = 1+ curr_freq.get(curr_word,0)
                if curr_freq[curr_word] > freq_count[curr_word]:
                    break
                j+=wordsize
            if j==i+winsize:
                res.append(i)
        return res
        