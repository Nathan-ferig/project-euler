def sum_by_trial(n: int = 1000, a: int=3, b: int=5) -> int:
    return sum(i for i in range(n) if (i % a ==0 or i % b == 0))

def sum_by_math(n: int = 1000, a: int=3, b: int=5) -> int:
    c = a * b
    return int((a/2)*(int((n-1)/a))*(int((n+a-1)/a)) + (b/2)*(int((n-1)/b))*(int((n+b-1)/b)) - (c/2)*(int((n-1)/c))*(int((n+c-1)/c)))

print(sum_by_trial(1000,2,7))
print(sum_by_math(1000,2,7))