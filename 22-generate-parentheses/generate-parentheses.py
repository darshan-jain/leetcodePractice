class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(o,close,curr):
            if o == close == 0:
                result.append(curr)
                return 
            if o > 0 :
                generate(o-1,close,curr+"(")
            if o < close:
                generate(o,close-1,curr+")")
        generate(n,n,"")
        return result
        