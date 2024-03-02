'''
Coderbyte: Bracket Combinations
Solution by James Errington, 2024

Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero,
and return the number of valid combinations that can be formed with num pairs of parentheses.
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()).
There are 5 total combinations when the input is 3, so your program should return 5.
'''
count = 0

def BracketCombinations(num: int) -> int:
    if num == 0:
        return 1
    global count
    count = 0
    branch(num * 2, 0, 0, "")
    return count

def branch(n: int, o: int, c: int, s: str):
    if n == 0:
        if o == c:
            global count
            count += 1
        return
    if len(s) == 0:
        branch(n - 1, o + 1, c, s+"(")
    else:
        branch(n - 1, o + 1, c, s+"(")
        if o > c:
            branch(n - 1, o, c + 1, s+")")

print(BracketCombinations(5) == 42)
print(BracketCombinations(4) == 14)
print(BracketCombinations(3) == 5)
print(BracketCombinations(2) == 2)
print(BracketCombinations(1) == 1)
print(BracketCombinations(0) == 0)
