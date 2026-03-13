
# first a approach with two pointer is more general
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


        return " ".join(s)
    

# second approach is more pythonic and simple
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(reversed(s))

# third approach is also simple but in O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        res = []
        for i in range(len(s)-1, -1, -1):
            res.append(s[i])
        return " ".join(res)
    