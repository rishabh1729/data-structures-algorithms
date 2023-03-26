# Head Recursion : When the recursion returns to the original calling function,
# there are still operations to be performed.
# Call stack is required in head recursion to keep track of calling functions, variables and values. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
