class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)
        if cnt["L"] > cnt["R"]:
            return cnt["L"] - cnt["R"] + cnt["_"]
        elif cnt["L"] < cnt["R"]:
            return cnt["R"] - cnt["L"] + cnt["_"]
        else:
            return cnt["_"]
        