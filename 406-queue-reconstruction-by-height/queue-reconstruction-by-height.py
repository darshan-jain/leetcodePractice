class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # N = len(people)
        # output = [None] * N
        # people.sort()

        # for height, q in people:
        #     i,j = 0,-1
        #     while i < N:
        #         if not output[i] or output[i][0] == height:
        #             j+=1
        #         if j==q:
        #             break
        #         i+=1
        #     output[i] = [height,q]
        # return output


        people = sorted(people, key = lambda x : (-x[0],x[1]))
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans