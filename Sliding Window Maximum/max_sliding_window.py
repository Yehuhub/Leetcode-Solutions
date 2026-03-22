
# my solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [(-num, index) for index, num in enumerate(nums)]
        res = []
        l, r = 0, k - 1
        heap = nums[l:r + 1]
        heapq.heapify(heap)
        while r < len(nums):
            heapq.heappush(heap, nums[r])
            while heap[0][1] > r or heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            l += 1
            r += 1
        return res
        

# neet code solution a bit more organized and clean, basically we only check for backwards in the window
# since we wont reach indexes to the right of the window ever
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
        

