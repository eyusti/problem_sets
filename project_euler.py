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

# problem 4
"""palindromes = []
for num_1 in range(999, 100, -1):
    for num_2 in range(999, 100, -1):
        # get string of number
        product = num_1 * num_2
        s_product = str(product)
        # get two strings to compare
        product_len = len(s_product)
        midpoint = int(product_len / 2)
        split_1 = s_product[0:midpoint]
        if product_len % 2 == 0:
            split_2 = s_product[midpoint:product_len]
        else:
            split_2 = s_product[midpoint+1:product_len]
        # check if palindrome
        temp_split_2 = list(reversed(split_2))
        fixed_split_2 = ''.join(temp_split_2)
        if split_1 == fixed_split_2:
            palindromes.append(product)
print(max(palindromes))"""

# problem 5
def smallest_multiple():
    c_num = 46189
    #highest_possible = 2 432 902 008 176 640 000
    while True:
        tracker = 0
        #print("c_num:" + str(c_num))
        for num in range(11,21):
            if c_num % num != 0:
                tracker += 1
                #print("num:" + str(num))
                #print("tracker:" + str(tracker))
            if num == 20 and tracker == 0:
                #print("!!!!!!!!!" + str(c_num))
                return c_num
            if tracker == 1:
                c_num += 46189
                break

print(smallest_multiple())
    




