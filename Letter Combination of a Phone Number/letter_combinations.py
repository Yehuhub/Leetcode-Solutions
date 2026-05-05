
# my solution, straightforward and runs good
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digit_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, cur):
            if i >= len(digits):
                res.append(cur)
                return

            for char in digit_to_char[digits[i]]:
                cur += char
                backtrack(i + 1, cur)
                cur = cur[:-1]

        backtrack(0, "")
        return res


# this solution is a bit cleaner as we dont actually mutate the cur object, 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digit_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, cur):
            if i >= len(digits):
                res.append(cur)
                return

            for char in digit_to_char[digits[i]]:
                backtrack(i + 1, cur + char) # here we dont mutate cur so in the next iteration we dont need to remove last char

        backtrack(0, "")
        return res