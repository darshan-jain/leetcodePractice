class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        aptr = 0 
        bptr = 0 
        asize = len(firstList)
        temp = [30,30]
        bsize=len(secondList)
        while aptr<asize and bptr < bsize:
            if secondList[bptr][0] <= firstList[aptr][1] and firstList[aptr][0] <= secondList[bptr][1]:
                temp[0] = max(firstList[aptr][0], secondList[bptr][0])
                temp[1] = min(firstList[aptr][1], secondList[bptr][1])
                print(temp)
                res.append(temp[:])
            if firstList[aptr][1] > secondList[bptr][1]:
                bptr+=1
            else:
                aptr+=1
        return res
