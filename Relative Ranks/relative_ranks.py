from typing import List

# intuitive solution, is a bit ugly but works as intended in O(nlogn)
class Solution:
    # def findRelativeRanks(self, score: List[int]) -> List[str]:
    #     places = dict()
    #     x = sorted(score, reverse=True)

    #     for i in range(len(x)):
    #         if i == 0:
    #             places[x[i]] = "gold"
    #         elif i == 1:
    #             places[x[i]] = "silver"
    #         elif i == 2:
    #             places[x[i]] = "bronze"
    #         else:
    #             places[x[i]] = str(i+1) + "th"

    #     result = []
    #     for num in score:
    #         result.append(places[num])
    #     return result
    
    # second solution works exactly the same but looks nicer
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x = sorted(score, reverse=True)
        top = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = {score: top[i] if i < 3 else str(i+1) for i, score in enumerate(x)}
        return [result[num] for num in score]
