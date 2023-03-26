# Tail Recursion : When the recursion returns to the original calling function,
# no operations (except return) need to be performed.
# Hence, call stack is not required in tail recursion / tail-call optimization.

def factorial(n, a):
    if n == 0 or n == 1:
        return a
    return factorial(n-1, n*a)

print(factorial(5, 1))
