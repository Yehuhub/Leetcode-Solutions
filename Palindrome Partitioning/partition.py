# what we need to understand here is that we are very basically going through all substrings, 
# and if we find a pali we add it
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(cur, i):
            if i >= len(s):
                res.append(cur[:])
                return

            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    cur.append(s[i:j+1])
                    backtrack(cur, j + 1)
                    cur.pop()

        backtrack([], 0)
        return res



    def is_pali(self, word, l, r):

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

    

        