# for loop
import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# recursive

def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)

start = time.time()
print('for loop:', factorial_iterative(10))
print('time taken for for loop:', (time.time() - start) * 1000000)

start = time.time()
print('recursive:', factorial_recursive(10))
print('time taken for recursive:', (time.time() - start) * 1000000)

# You almost never use recursion for performance reasons. You use recursion to make the problem more simple.
# https://stackoverflow.com/questions/9386375/efficiency-recursion-vs-loop