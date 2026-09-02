class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = [0]*4 
        hm = {
            "U":0,
            "D":1,
            "L":2,
            "R":3
        }
        for c in moves:
            cnt[hm[c]]+=1
        
        if cnt[0]==cnt[1] and cnt[2]==cnt[3]:
            return True
        return False

        