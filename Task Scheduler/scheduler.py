
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
    

# this a faster solution O(n)
# the idea here is that the max task sets how many idles we have.
# then we can reduce by the occurences of the other tasks.
# whats important here is the min in the for loop, it basically says, if the occurences of a task are
# less than the empty spaces we have you can just reduce them, otherwise it means we dont have enough empty spaces,
# so we can only reduce the empty space the max val has
# this solution is less intuitive
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = [0] * 26

        for task in tasks:
            char_map[ord(task) - ord('A')] += 1

        char_map.sort(reverse=True)
        max_val = char_map[0] - 1
        idle_count = (max_val) * n
        for i in range(1, 26):
            idle_count -= min(char_map[i], max_val)

        return idle_count + len(tasks) if idle_count > 0 else len(tasks)