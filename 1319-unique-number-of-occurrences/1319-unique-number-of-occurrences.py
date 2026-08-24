class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        seen = set()
        for k,v in cnt.items():
            if v in seen:
                return False 
            seen.add(v)
        return True

        