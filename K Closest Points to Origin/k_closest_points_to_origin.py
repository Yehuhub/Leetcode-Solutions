from typing import List
import math
import heapq
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first solution using sort
        # distances = [(math.dist((0,0), (x,y)), [x,y]) for x,y in points]
        # distances = sorted(distances, key=lambda i: i[0])
        # return [distances[i][1] for i in range(k)]

        # this is a good solution but it runs in O(nlogn)
        # we can further optimize it using min heap, that way we get O(klogn)
        # as we remove k elements from the heap and each pop is in O(logn)

        distances = [(math.dist((0,0), (x,y)), [x,y]) for x,y in points]
        heapq.heapify(distances)

        return [heapq.heappop(distances)[1] for i in range(k)]