
# this is a tricky and interesting question.
# basically the trick her is to find how many hours it takes for koko to eat a pile, and we calculate
# that using ceiling of piles[i] / k, once we understand that we can use binary search to find the
# min number that satisfy that condition, in which the time it takes to sum up all the array is <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:   
        n = len(piles)
        lower_bound = 1
        upper_bound = max(piles)
        res = 0

        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2    

            eaten = 0
            for i in range(n):
                eaten += math.ceil(piles[i] / k)
            if eaten > h:
                lower_bound = k + 1
            elif eaten <= h:
                res = k
                upper_bound = k - 1
        return res