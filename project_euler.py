# problem 1
"""sum = 0
for number in range(0, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
print(sum)"""

# problem 2
def problem_2():
    total = 0
    num1 = 1
    num2 = 1
    new_value = 0

    while new_value < 4000000:

        new_value = num1 + num2

        if new_value % 2 == 0:
            total += new_value

        num1 = num2
        num2 = new_value
    
    print(total)

def fib_rec(n):
    if n <= 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_generator():
    f1 = 1
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f2 + f1

def foo():
    yield 1
    print("here")
    yield 3
    print("done")

import itertools
fib_up_to_n = itertools.takewhile(lambda f: f < 40000000, fib_generator())
for x in fib_up_to_n:
    print("a", x)

# problem 3

