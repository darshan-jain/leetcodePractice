class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()

        def count1bit(val):
            cnt = 0 
            for c in val:
                if c =="1":
                    cnt+=1
            return cnt
        hm = defaultdict(list)
        for num in arr:
            binval = str(bin(num)[2:])
            cc = count1bit(binval)
            hm[cc].append(num)
        
        sorted_dict = dict(sorted(hm.items()))
        res = []
        for k,v in sorted_dict.items():
            for val in v:
                res.append(val)
        print(hm)
        return res

        