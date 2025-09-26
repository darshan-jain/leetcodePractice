from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.data = defaultdict(list) # person->[(time, userId)]
        self.time = 0 
        self.graph = defaultdict(list) #networkgraph
        self.maxheap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.data[userId].append((-1*self.time, tweetId))    

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        #that person's tweets 
        for time, tid in self.data[userId]:
            heapq.heappush(self.maxheap, (time, userId, tid))

        #their followers tweets
        for uid in self.graph[userId]:
            if uid != userId:
                for time, tid in self.data[uid]:
                    heapq.heappush(self.maxheap, (time, uid, tid))
      
        k=10
        while k>0 and self.maxheap:
            t,uuid, tid = heapq.heappop(self.maxheap)
            res.append(tid)
            k-=1
        self.maxheap = []
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        #can't follow themselves
        if followeeId not in self.graph[followerId]:
            self.graph[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)