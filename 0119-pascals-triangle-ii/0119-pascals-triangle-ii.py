class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_level = [0] * (len(res)+1)
            for j in range(len(res)):
                next_level[j]+=res[j]
                next_level[j+1]+=res[j]
            res = next_level
        return res
        