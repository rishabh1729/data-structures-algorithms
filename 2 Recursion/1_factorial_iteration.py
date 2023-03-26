def factorial(n):
    if n == 0 or n == 1:
        return 1
    p = 1
    for i in range(2, n+1):
        p = p * i
    return p

print(factorial(5))
