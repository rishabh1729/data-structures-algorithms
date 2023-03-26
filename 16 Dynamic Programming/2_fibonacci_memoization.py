# Fibonacci : Top-down Dynamic Programming
# Recursion with memoization

def fibonacci(n):
    if f[n] == -1:
        if n == 0 or n == 1:
            f[n] = n
        else:
            f[n] = fibonacci(n-1) + fibonacci(n-2)
    return f[n]

if __name__ == '__main__':
    n = 3
    f = [-1]*(n+1)
    print(fibonacci(n))
