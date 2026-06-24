'''
str = "{[([{}])]}"

'''
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack:
                return False

            top = stack.pop()
            if top != pairs[char]:
                return False

    return len(stack) == 0

expr = "{[()()]}"
print(is_balanced(expr))

