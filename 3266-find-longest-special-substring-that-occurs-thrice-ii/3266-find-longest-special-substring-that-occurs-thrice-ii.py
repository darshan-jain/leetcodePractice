class Solution:
    def maximumLength(self, s: str) -> int:

        arr = [[-1,-1,-1] for _ in range(26)]
        lastseen = '*'
        winLen = 0 

        for c in s:
            idx = ord(c) - ord('a')
            winLen = winLen + 1 if lastseen == c else 1
            lastseen = c

            minIdx = arr[idx].index(min(arr[idx]))
            if winLen > arr[idx][minIdx]:
                arr[idx][minIdx] = winLen
            

        print(arr)
        res = -1
        for i in range(len(arr)):
            res = max(res, min(arr[i]))
        return res

        