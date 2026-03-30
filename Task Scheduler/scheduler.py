
# this is quite tough
# basically whenever we pull a task from the heap we insert it to the queue with the next time it could run
# so current time + n, then whenever the first inserted task to the q is ready to be performed we pull it out 
# and insert it into the heap
# so the idea is that all tasks that can be performed are in the heap, and task that wait are in the q
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = Counter(tasks)
        heap = [-freq for val, freq in heap.items()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if heap:
                task = -heapq.heappop(heap)
                if task - 1 > 0:
                    q.append((task - 1, time + n))
            if q and q[0][1] <= time:
                task = q.popleft()
                heapq.heappush(heap, -task[0])
            
        return time