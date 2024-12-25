class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # d = {}
        # for num in arr:
        #     d[num] = 0 
        # for num in arr:
        #     d[num] +=1
        # seen = set()
        # for key,value in d.items():
        #     if value in seen:
        #         return False
        #     seen.add(value)
        
        # return True

        counts = defaultdict(int)
        for num in arr:
            counts[num]+=1
        occur = list(counts.values())
        return len(occur) == len(set(occur))


        