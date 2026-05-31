class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]

        def next_permutation(arr):
            i = len(arr) - 2

            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1

            if i >= 0:
                j = len(arr) - 1
                while arr[j] <= arr[i]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]

            l, r = i + 1, len(arr) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        for _ in range(k - 1):
            next_permutation(nums)

        return "".join(map(str, nums))