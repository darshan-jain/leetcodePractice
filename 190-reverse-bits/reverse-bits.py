class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        revn =0 
        for _ in range(32):
            revn = revn <<1
            bit = n&1
            revn = revn | bit
            n = n>>1
        return revn
        