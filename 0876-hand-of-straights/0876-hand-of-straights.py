from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        dic = defaultdict(int)
        res = []
        path = []
        for num in hand:
            dic[num] = dic.get(num,0)+1 
        dic = dict(sorted(dic.items()))
        #print(dic)
        for k,v in dic.items():
            minV = k 
            break
        while dic:
            path = []
            for i in range(minV,minV + groupSize):
                if i in dic:
                    path.append(i)
                    dic[i]-=1
                    if dic[i]==0:
                        del dic[i]
                else:
                    return False
            if dic:
                minV = list(dic.keys())[0]
            res.append(path)
        print(res)
        return True

        


        