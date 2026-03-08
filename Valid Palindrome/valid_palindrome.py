
# this is a good solution in O(n) runtime and space, can be made in O(1) runtime with more checks for alphanum
# in the while loop

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(pal) - 1

        while left < right:
            if pal[left] != pal[right]:
                return False
            left += 1
            right -= 1
            
        return True