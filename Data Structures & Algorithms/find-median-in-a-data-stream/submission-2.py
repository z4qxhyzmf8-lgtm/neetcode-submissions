class MedianFinder:

    def __init__(self):
        self.left = [] #max_heap for num to left of median
        self.right = [] #min_heap for num to right of median
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        if not self.left:
            self.left.append(-num)
            return 

        if not self.right:
            if -self.left[0] <= num:
                self.right.append(num)
            else:
                val = -self.left.pop()
                self.left.append(-num)
                self.right.append(val) 
            return

        if num <= -self.left[0]:
            if abs(len(self.left) - len(self.right)) >= 1: 
                val = -heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, val)
            else:
                heapq.heappush(self.left, -num)
        elif self.right[0] <= num:
            if abs(len(self.left) - len(self.right)) < 1:
                val = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -val)
            else:
                heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        print(self.left)
        print(self.right)
        

    def findMedian(self) -> float:
        if self.count % 2:
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
        
        