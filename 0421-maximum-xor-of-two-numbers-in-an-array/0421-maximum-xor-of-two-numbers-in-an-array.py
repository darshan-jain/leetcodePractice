class TrieNode():
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insertbits(self, num):
        bits = bin(num)[2:].zfill(32)
        node = self.root 
        for bit in bits:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def findmaxXOR(self, num):
        bits = bin(num)[2:].zfill(32)
        node = self.root 
        maxxor = ''
        for bit in bits:
            if bit =='0':
                oppo_bit='1'
            elif bit=='1':
                oppo_bit ='0'
            
            if oppo_bit in node.children:
                maxxor += oppo_bit 
                node = node.children[oppo_bit]
            else:
                maxxor += bit 
                node = node.children[bit]
        return int(maxxor,2) ^ num

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insertbits(num)
        
        max_ = 0 
        for num in nums:
            max_ = max(max_, self.findmaxXOR(num))
        return max_