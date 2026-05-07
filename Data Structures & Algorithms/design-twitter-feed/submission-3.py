class Twitter:

    def __init__(self):
        self.posts = defaultdict(deque) #user_id ->[count, post_id]
        self.followers = defaultdict(set) #user_id -> set of followers 
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.posts[userId].append([self.counter, tweetId])
        if len(self.posts[userId]) > 10:
            self.posts[userId].popleft()


    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        feed = []
        for time, post in self.posts[userId]:
            heapq.heappush(min_heap, [time, post])
        for follower in self.followers[userId]:
            if len(min_heap) < 10:
                for time, post in self.posts[follower]:
                    heapq.heappush(min_heap, [time, post])
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)
                continue
            if self.posts[follower][-1] < min_heap[0][0]:
                continue
            else:
                count = 0
                n = len(self.posts[follower])
                while count < n and self.posts[follower[-1]] < min_heap[0][0]:
                    count += 1
                    heapq.heappop(min_pop)
                    time, post = self.posts[follower].pop()
                    heapq.heappush([time, post])
                    self.posts[follower].appendleft([time, post])
                while count < n:
                    count += 1
                    time, post = self.posts[follower].pop()
                    self.posts[follower].appendleft([time, post])
        while min_heap:
            time, post = heapq.heappop(min_heap)
            feed.append(post)
        feed.reverse()
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

       
        
