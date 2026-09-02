class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = list(moves)
        cnt = Counter(moves)
        if cnt["L"] == cnt["R"] and cnt["U"]==cnt["D"]:
            return True
        else:
            return False
        