## RECURSION ##

def factorial(n):
    assert n >= 0 and int(n) == n , "The value of n should be positive!!"
    if n == 0:
        return 1
    else:
        result = factorial(n - 1)
        return result * n
    
print(factorial(10))


def fibonacci(n):
    assert n>=0 and int(n) == n, "The number should be positive!"
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))