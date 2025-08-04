

def isValid(s: str) -> bool:
    mapping = { '}': '{', ']': '[', ')': '('} # we create a hashmap so that we can check for match in o(1)

    stack = [] # create a stack

    for char in s:
        if char in mapping: # if char is a closing parentheses
            x = stack.pop() if stack else '#' # pop the opening parantheses from the stack
            if mapping[char] != x: # if the closing parantheses does not match the opening return False
                return False
        else:
            stack.append(char) # insert the open parantheses to the stack

    # if stack is not empty it means we have an extra opening parantheses that werent matched
    return not stack

# this is the same problem only now adding a new type of parantheses - '|', '|' is a unique parantheses but
# it is the char for open or closed
def isValidExtra(s: str) -> bool:
    mapping = { '}': '{', ']': '[', ')': '('}

    stack = []

    for char in s:
        if char in mapping: 
            x = stack.pop() if stack else '#'
            if mapping[char] != x:
                return False
            
        elif char == '|':
            # we peek into the last inserted item to the stack
            # if the last item matches to '|' it means we can safely call the current one a closing '|'
            if stack and stack[-1] == '|': 
                stack.pop()
            else:
                stack.append(char)
            
        else:
            stack.append(char)

    return not stack
