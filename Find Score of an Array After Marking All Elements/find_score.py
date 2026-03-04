
from typing import List
import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap = [(val, index) for index, val in enumerate(nums)]
        heapq.heapify(min_heap)
        
        removed = set()
        total = 0

        while min_heap:
            val, i = heapq.heappop(min_heap)
            if i not in removed:
                total += val
                removed.add(i)
                removed.add(i+1)
                removed.add(i-1)

        return total
        
# the idea is that we create a min heap, then each time we pop from the heap we get the smallest item
# then we add the neighbors it and its neighbors into the removed set
# each item in the removed set is not processed, so acts like it is removed.