# first solution we sort the array so that when we got a combination that starts with a specific candidate,
# we can skip to the next number that is not that candidate
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i+1, cur, total+candidates[i])

            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i+1, cur, total)

        backtrack(0, [], 0)
        return res
    
# this is the same solution but using a for loop to eliminate duplicates instead of the while loop 
# in the other solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, cur, total):
            if total == target:
                res.append(cur[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    return
                
                cur.append(candidates[i])
                backtrack(i + 1, cur, candidates[i] + total)
                cur.pop()

        backtrack(0, [], 0)
        return res