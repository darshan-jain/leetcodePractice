class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        news = s+s
        if s in news[1:-1]:
            return True
        return False
        