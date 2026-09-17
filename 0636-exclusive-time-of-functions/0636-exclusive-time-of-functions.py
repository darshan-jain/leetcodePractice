class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        res = [0] * n 
        prev = 0 
        for log in logs:
            log = log.split(":")
            log[0] = int(log[0])
            log[2] = int(log[2])
            if log[1]=="start":
                if stack:
                    res[stack[-1]]+=log[2]-prev
                stack.append(log[0])
                prev = log[2]
            else:
                res[stack.pop()]+=log[2] - prev+1
                prev = log[2]+1
        return res
        