from typing import List
from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        self.time=0 # counter to simulate time for tweets
        self.tweets = defaultdict(list) #  Each user has a deque of their tweets (tweetId, time)
        self.followees = defaultdict(set)  # Each user has a set of followees


    def postTweet(self, userId: int, tweetId: int) -> None:
        # Each user can post tweets; we append the tweet with current time
        self.time += 1
        if len(self.tweets[userId]) < 10:
            heapq.heappush(self.tweets[userId], (self.time, tweetId))
        else:
            # If there are already 10 tweets, use heappushpop to maintain only the most recent 10 tweets
            heapq.heappushpop(self.tweets[userId], (self.time, tweetId))
    def getNewsFeed(self, userId: int) -> list:
        # Collect the user's own tweets and their followees' tweets
        all_tweets = list(self.tweets[userId])
        
        for followeeId in self.followees[userId]:
            all_tweets.extend(self.tweets[followeeId])

        # Use heapq.nlargest to get the 10 most recent tweets by timestamp
        most_recent_tweets = heapq.nlargest(10, all_tweets, key=lambda x: x[0])

        # Extract only the tweet IDs to return
        return [tweet[1] for tweet in most_recent_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # Cannot follow oneself
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)



twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts tweet 5
print(twitter.getNewsFeed(1))  # Should return [5]
twitter.follow(1, 2)  # User 1 follows user 2
twitter.postTweet(2, 6)  # User 2 posts tweet 6
print(twitter.getNewsFeed(1))  # Should return [6, 5]
twitter.unfollow(1, 2)  # User 1 unfollows user 2
print(twitter.getNewsFeed(1))  # Should return [5]

twitter.postTweet(1, 5)  # User 1 posts tweet 5
print(twitter.getNewsFeed(1))  # [5]

twitter.follow(1, 2)  # User 1 follows User 2
twitter.postTweet(2, 6)  # User 2 posts tweet 6
print(twitter.getNewsFeed(1))  # [6, 5]

twitter.unfollow(1, 2)  # User 1 unfollows User 2
print(twitter.getNewsFeed(1))  # [5]
