class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            numstr = str(num)
            for c in numstr:
                res.append((int(c)))
        return res
        