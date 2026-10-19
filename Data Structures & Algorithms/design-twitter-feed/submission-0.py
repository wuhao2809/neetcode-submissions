from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> [(time, tweetId), ...]
        self.following = defaultdict(set)  # userId -> {followeeId, ...}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        # 每个人先放入自己的最新一条推文
        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweet_id = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweet_id, uid, index))

        feed = []

        while heap and len(feed) < 10:
            _, tweet_id, uid, index = heapq.heappop(heap)
            feed.append(tweet_id)

            # 这个人的下一条候选推文，是他更早的那一条
            if index > 0:
                prev_time, prev_tweet_id = self.tweets[uid][index - 1]
                heapq.heappush(
                    heap,
                    (-prev_time, prev_tweet_id, uid, index - 1)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)