class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ops = sorted(zip(indices, sources, targets), reverse=True)
        
        for idx, src, tgt in ops:
            # Check if the source substring matches the original string at idx
            if s[idx : idx + len(src)] == src:
                # Slice and replace the substring with the target
                s = s[:idx] + tgt + s[idx + len(src):]
                
        return s
        