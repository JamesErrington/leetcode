'''
Coderbyte: Bracket Matcher
Solution by James Errington, 2024

Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for.
Otherwise return 0.
For example: if str is "(hello (world))", then the output should be 1,
but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up.
Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
'''

def BracketMatcher(strParam: str) -> int:
    stack = []
    for char in strParam:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0: return 0
            stack.pop()

    if len(stack) > 0:
        return 0
    return 1


print(BracketMatcher("(coder)(byte))") == 0)
print(BracketMatcher("(c(oder)) b(yte)") == 1)
print(BracketMatcher("(hello (world))") == 1)
print(BracketMatcher("((hello (world))") == 0)
print(BracketMatcher("hello") == 1)
