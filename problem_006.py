"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def Sum_Of_Squares(max_number: int = 10, min_number: int = 1) -> int:
    sum: int = 0
    for i in range(min_number,max_number+1):
        sum += i*i
    return sum

def Square_Of_Sum(max_number: int = 10, min_number: int = 1) -> int:
    sum: int = 0
    for i in range(min_number,max_number+1):
        sum += i
    sum *= sum
    return sum

def Difference(max_number: int = 10, min_number: int = 1) -> int:
    return Square_Of_Sum(max_number,min_number) - Sum_Of_Squares(max_number,min_number)

print(Difference(100))
