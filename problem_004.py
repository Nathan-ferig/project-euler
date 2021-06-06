"""
Find the largest palindrome made from the product of two 3-digit numbers.


a  = 102
b = str(a)
print(b)
print(b[::-1])
"""

def largest_palindrome():
    palindrome = []
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            mult = i*j
            string = str(mult)
            if (string == string[ : : -1]):
                palindrome.append(mult)
    return max(palindrome)
    
print(largest_palindrome())