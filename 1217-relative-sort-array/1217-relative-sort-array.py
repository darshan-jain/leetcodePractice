class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm = Counter(arr1)
        i=0
        for ele in arr2:
            count = hm[ele]
            for _ in range(count):
                arr1[i]=ele
                i+=1
            del hm[ele]
        
        for k,v in sorted(hm.items()):
            for _ in range(v):
                arr1[i]=k
                i+=1
        return arr1
            
        