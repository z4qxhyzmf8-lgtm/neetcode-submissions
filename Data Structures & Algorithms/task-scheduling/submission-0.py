class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #no cooldown so we schedule in whatever order we want
        if n == 0:
            return len(tasks)
        
        #compute frequency of each task
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1 
        
        #make a heap out of the tasks, since most freq task we
        #want to do first
        max_heap = [-freq[key] for key in freq]
        heapq.heapify(max_heap)
        
        count = 0
        q = deque() #stores pairs[freq, time_next_available]
        while max_heap or q:
            count += 1

            #if there are still available tasks we process them
            if max_heap:
                f = -heapq.heappop(max_heap) - 1

                #if current task needs to be done later we add it to q
                if f > 0:
                    q.append([f, count + n])
            
            #no more unique task in heap so we skip time
            else:
                count = q[0][1]
            
            #if we have tasks in q and enough time passed, add them back to heap
            if q and q[0][1] == count:
                task, time = q.popleft()
                heapq.heappush(max_heap, -task)
        return count
            

            
        

        