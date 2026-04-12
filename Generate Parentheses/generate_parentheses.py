
# my solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur_bckts, cur_open, finished):
            if finished == n: # if we closed enough brackets
                res.append(cur_bckts)
                return
            if cur_open > n: # if we opened too many brackets
                return

            # we haven't opened too many meaning we definitely have the option to open
            cur_bckts += '(' 
            backtrack(cur_bckts, cur_open + 1, finished)
            
            # only if we open brackets we can close
            if cur_open > 0 and finished < cur_open:
                # we remove the open bracket we added in the last call
                # and we add a closing bracket
                cur_bckts = cur_bckts[:-1] + ')' 
                backtrack(cur_bckts, cur_open, finished + 1)

        backtrack("", 0, 0)
        return res
    
# just a bit cleaner but same idea
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur_bckts, open_bckts, finished):
            if finished == n:
                res.append(cur_bckts)
                return
            
            if open_bckts < n:
                cur_bckts += '('
                backtrack(cur_bckts, open_bckts + 1, finished)
                cur_bckts = cur_bckts[:-1]

            if finished < open_bckts:
                cur_bckts += ')'
                backtrack(cur_bckts, open_bckts, finished + 1)
                cur_bckts = cur_bckts[:-1]
        
        backtrack("", 0, 0)
        return res