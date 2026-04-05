
# we keep two heaps, one holds the large elements(min heap) and one holds the small elements(max heap)
# that way we can easily find the middle of the elements, if its even we take the max and min,
# if its odd we take either the min or max depending on which heap is larger.
# the key thing here is that on insert we have to balance the heaps
class MedianFinder: 

    def __init__(self):
        self.min_heap = [] # the min heap is elements larger than mid
        self.max_heap = [] # the max heap is elements smaller than mid

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                item = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -item)
            else:
                item = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, item)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
        
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        return -self.max_heap[0]
