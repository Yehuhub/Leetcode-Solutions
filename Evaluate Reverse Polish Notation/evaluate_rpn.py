
# this is the optimal solution, runs in O(n) time and space
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                y = stack.pop()
                x = stack.pop()
                res = self.calc(x, y, tokens[i])
                stack.append(res)

        return stack.pop()
        
    def calc(self, x: int, y: int, op: str):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return int(x / y)
        

# this is a recursive solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def recurse():
            x = tokens.pop() # we pop an element from the list
            if x not in "+-/*": # means we reached all the way in the recursion, and we need to return this number for calculation
                return int(x)
            
            right = recurse() # we first get the right, since we are using a stack, we first pop the second element of the equasion
            left = recurse()

            if x ==  "+": return left + right
            elif x == "-": return left - right
            elif x == "*": return left * right
            elif x == "/": return int(left / right)

        return recurse()
                