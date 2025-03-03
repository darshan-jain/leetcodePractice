class Solution:
    def reverseBits(self, n: int) -> int:
        revn = 0 
        for _ in range(32):
            revn = revn << 1
            bit = n&1
            revn = revn | bit
            n = n>>1
        return revn
        