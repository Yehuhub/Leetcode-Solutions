class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # this solution uses a heap, this way we can easily pop the first k element from the heap and
        # be done with it
        # counter = Counter(nums)
        # counter = [(-freq, val) for val, freq in counter.items()]
        
        # heapq.heapify(counter)
        # res = []
        # for i in range(k):
        #     freq, val = heapq.heappop(counter)
        #     res.append(val)
        # return res


        # this solution use some sort of bucket sort for a better runtime at O(n).
        # we count appearances of each num, then we create n(len of the array) buckets, 
        # each index in the array is the amount of appearances of some value, then we add the value into
        # a list in that bucket.
        # after we got the bucket we iterate back to front on the buckets array and just take the first k
        # elements we encounter
        counter = Counter(nums)
        bucket_arr = [[] for _ in range(len(nums))] 

        for val, freq in counter.items():
            bucket_arr[freq - 1].append(val)

        res = []

        for l in bucket_arr[::-1]:
            for num in l:
                res.append(num)
                k -= 1
                if k <= 0:
                    return res



