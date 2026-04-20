"""
 we want to greedily always place the most frequent char.
 but we run into a problem when we have one really frequent char and a lot of others after it, for example:
 aaabc
 we have a=3, b=1, c=1, so if we just always take the most frequent char we get, aaabc which is not goot
 so instead we pick the most frequent char, we place it in the string and put away, that way on the next round
 we get to take the second most frequent char.
 and after that we place it back in the heap

 i think the difficult part in this question is understanding the exit condition.
"""

"""
aaa
"a", then we put it in prev,
now heap is empty, but prev has two more a's, so its impossible
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        occ = Counter(s)

        heap = [(-count, char) for char, count in occ.items()]
        res = ""

        heapq.heapify(heap)

        prev = None
        while heap or prev: 
            if not heap and prev:
                return ""

            cnt, char = heapq.heappop(heap)
            res += char

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt + 1 < 0:
                prev = (cnt + 1, char)

        return res