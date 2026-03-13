
# interesting problem involving stack
class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        sign = 1
        stack = []
            
        for char in s:
            # if it is a digit we first need to find the number
            if char.isdigit():
                cur = cur * 10 + int(char)

            # if char is + or -, we add the last number we got to(multiplied by sign to know if add or sub)
            # than we save the new sign we got to and reset the number
            elif char in "+-":
                res += sign * cur 
                sign = 1 if char == "+" else -1
                cur = 0

            # we got to a new bracket, we want to save the result weve achieved so far along with the sign that
            # came before the brackets
            # that way we can pop it when we reach the end of this brackets
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                cur = 0
                sign = 1

            # we grab the previous result and add it to the result weve achieved inside the brackets
            elif char == ')':
                res += cur * sign
                res *= stack.pop()
                res += stack.pop()

                cur = 0
            
        # here we need to add the last number and sign that we got to the last res
        return res + cur * sign