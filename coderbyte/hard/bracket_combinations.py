'''
Coderbyte: Bracket Combinations
Solution by James Errington, 2024

Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero,
and return the number of valid combinations that can be formed with num pairs of parentheses.
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()).
There are 5 total combinations when the input is 3, so your program should return 5.
'''

def BracketCombinations(num: int) -> int:
    str = "()" * num
    print(str)
    return 1

# 5 42
# 4 14
# print(BracketCombinations(3) == 5) # ()()(), ()(()), (())(), ((())), (()())
# print(BracketCombinations(2) == 2) # ()(), (())
# print(BracketCombinations(1) == 1) # ()
# print(BracketCombinations(0) == 0)


'''
1: 1
2: 1 + 1
3: 1 + 2 + 2
4: 1 + 2 + 5 + 6
5: 1 + 2 + 5 + 14 + 20
'''
