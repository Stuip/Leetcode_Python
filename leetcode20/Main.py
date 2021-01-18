def isValid(s):
    stack = list(s)
    if len(stack) == 0:
        return True
    tempStack = ['?']
    for value in stack:
        # value = stack.pop()
        if value == '(' or value == '[' or value == '{':
            tempStack.append(value)
        elif value == ')':
            temp = tempStack.pop()
            if temp != '(':
                return False
        elif value == ']':
            temp = tempStack.pop()
            if temp != '[':
                return False
        elif value == '}':
            temp = tempStack.pop()
            if temp != '{':
                return False
    return len(tempStack) == 1


s = "()"
print(isValid(s))