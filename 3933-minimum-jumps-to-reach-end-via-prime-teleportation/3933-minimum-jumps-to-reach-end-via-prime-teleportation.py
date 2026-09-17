from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # prime -> indices whose value is divisible by prime
        prime_indices = defaultdict(list)

        def isPrime(num):
            if num <= 1:
                return False

            if num == 2:
                return True

            if num % 2 == 0:
                return False

            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2

            return True

        def getPrimeFactors(num):
            factors = []

            if num % 2 == 0:
                factors.append(2)
                while num % 2 == 0:
                    num //= 2

            p = 3
            while p * p <= num:
                if num % p == 0:
                    factors.append(p)

                    while num % p == 0:
                        num //= p

                p += 2

            if num > 1:
                factors.append(num)

            return factors

        # Same idea as your graph construction,
        # but instead of scanning the entire nums array,
        # directly store indices for each prime factor.
        for i, num in enumerate(nums):
            for p in getPrimeFactors(num):
                prime_indices[p].append(i)

        q = deque([(0, 0)])
        visit = {0}

        while q:
            idx, step = q.popleft()

            if idx == n - 1:
                return step

            # Normal move: idx - 1
            if idx - 1 >= 0 and idx - 1 not in visit:
                visit.add(idx - 1)
                q.append((idx - 1, step + 1))

            # Normal move: idx + 1
            if idx + 1 < n and idx + 1 not in visit:
                visit.add(idx + 1)
                q.append((idx + 1, step + 1))

            # IMPORTANT:
            # Only a PRIME number can make the special jump
            if isPrime(nums[idx]):

                p = nums[idx]

                if p in prime_indices:

                    for j in prime_indices[p]:
                        if j not in visit:
                            visit.add(j)
                            q.append((j, step + 1))

                    # We never need to process this prime again
                    del prime_indices[p]

        return n - 1