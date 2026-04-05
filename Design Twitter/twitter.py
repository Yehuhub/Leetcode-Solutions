
# the solution is similar to merge k lists, we keep a heap of 10 most recent tweets, on each removal
# we add the next tweet from that user, that way if one user has all the most recent tweets we still
# have them in the heap.
class Twitter:

    def __init__(self):
        self.count = 0
        self.followees_map = defaultdict(set)
        self.tweet_map = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followees_map[userId].add(userId)
        for followee in self.followees_map[userId]:
            if followee in self.tweet_map:
                index = len(self.tweet_map[followee]) - 1
                count, tweet = self.tweet_map[followee][index]
                heapq.heappush(heap, (count, tweet, followee, index))

        while heap and len(res) < 10:
            count, tweet, followee, index = heapq.heappop(heap)
            res.append(tweet)
            if index - 1 >= 0:
                count, tweet = self.tweet_map[followee][index - 1]
                heapq.heappush(heap, (count, tweet, followee, index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees_map[followerId].discard(followeeId)
        
