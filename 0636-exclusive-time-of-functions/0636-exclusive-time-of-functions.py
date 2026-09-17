class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        s = []
        arr = [0]*n
        for log in logs:
            lst = log.split(":") #id, start/end, timestamp
            if lst[1]=="start":
                s.append([int(lst[0]), lst[1], int(lst[2]) ] )
            else:
                # same id or diff id 
                if int(lst[0])==s[-1][0]:
                    time = int(lst[2]) - s[-1][2] + 1
                    arr[s[-1][0]]+=time
                    s.pop()
                    if s:
                        s[-1][2]+=time
                
                # else: #mostly shouldn't go to this case
                #     s.append((int(lst[0]), lst[1], int(lst[2]) ) )
        return arr

        