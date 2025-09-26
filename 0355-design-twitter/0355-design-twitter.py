from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.data = [] # [time, userID,tweetID]
        self.time = 0 
        self.graph = defaultdict(list)
        self.maxheap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        temp = []
        temp.append(-1*self.time)
        temp.append(userId)
        temp.append(tweetId)
        self.data.append(temp)
       

        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for time,uid,tweetId in self.data:
            if uid == userId or uid in self.graph[userId]:
                heapq.heappush(self.maxheap, (time, uid, tweetId))
      
        k=10
        while k>0 and self.maxheap:
            t,uuid, tid = heapq.heappop(self.maxheap)
            res.append(tid)
            k-=1
        self.maxheap = []
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        #can't follow themselves
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