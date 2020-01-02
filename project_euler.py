# problem 1
"""sum = 0
for number in range(0, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
print(sum)"""

# problem 2
"""def problem_2():
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
    
    print(total)"""

# problem 3
"""number = 600851475143

def smallest_factor(num):
    for possible_factor in range(2,number):
        if number % possible_factor == 0:
            return possible_factor

while True:
    divisor = smallest_factor(number)
    if divisor is None:
        break
    new_number = number / divisor
    number = int(new_number)
    print(number)"""
