class Twitter:

    def __init__(self):
        self.feed = []
        self.users = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        following = self.users.get(userId, set()) | {userId}
        for time, tweetId, uid in reversed(self.feed):
            if uid in following:
                newsFeed.append(tweetId)
                if len(newsFeed) == 10:
                    break
        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, set()).add(followeeId)       
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, set()).discard(followeeId)
