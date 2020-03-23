# problem 1
"""sum = 0
for number in range(0 1000):
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
    for possible_factor in range(2number):
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
for num_1 in range(999 100 -1):
    for num_2 in range(999 100 -1):
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
"""def smallest_multiple():
    c_num = 46189
    #highest_possible = 2 432 902 008 176 640 000
    while True:
        tracker = 0
        #print("c_num:" + str(c_num))
        for num in range(1121):
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

print(smallest_multiple())"""

# problem 6

"""sum_of_squares = 0
square_of_sums = 0

#sum of squares
for num in range (1101):
    sum_of_squares += num**2

#square of sums
for num in range (1101):
    square_of_sums += num

print((square_of_sums**2)-sum_of_squares)"""

# problem 7
"""list_of_primes = [23571113]
current_number = 15

def is_prime(test_num):
    for num in range(3test_num):
        if test_num % num == 0:
            return False
    return True

while len(list_of_primes) <= 10001:
    prime_test = is_prime(current_number)
    if prime_test:
        list_of_primes.append(current_number)
        current_number += 2
    else:
        current_number += 2
print(list_of_primes[10000])"""

# problem 8
"""index = 0
max_product = 0
thousand_digit_num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
s_thousand_digit_num = str(thousand_digit_num)

while index <= 987:
    parsing = list(s_thousand_digit_num[index:index+13])
    num_parsing = [int(item) for item in parsing]
    temp_product = 1
    for num in num_parsing:
        temp_product = temp_product * num
    if temp_product > max_product:
        max_product = temp_product
    index += 1

print(max_product)"""

# problem 9
"""import math
def special_pythagorean_triplet():
    for a in range(1333):
        for b in range (a+1500):
            c = math.sqrt(a**2+b**2)
            print(a)
            print(b)
            print(c)
            if a**2+b**2 == c**2 and b > a and c > b and a + b + c == 1000:
                return(a*b*c) 

print(special_pythagorean_triplet())"""
               
# problem 10
"""primes = [3]
primes_checked = 0
for integer in range(520000002):
    print(integer)
    primes_checked = 0
    for prime in primes:
        if integer % prime == 0:
            break
        if integer % prime != 0:
            primes_checked += 1
        if primes_checked == len(primes):
            primes.append(integer)
            break

answer = sum(primes)+2
print(answer)
"""

# problem 11
grid = [
[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

max_row = 0
max_column = 0
max_diagonal = 0
"""
for row in grid:
    index = 0
    while index <= 16:
        product = row[index]*row[index+1]*row[index+2]*row[index+3]
        if product > max_row:
            max_row = product
        index+=1

print(max_row)
#48,477,312
"""
"""
for c_index in range(20):
    column_list = []
    for r_index in range(20):
        column_list.append(grid[r_index][c_index])
    index = 0
    while index <= 16:
        product = column_list[index]*column_list[index+1]*column_list[index+2]*column_list[index+3]
        if product > max_column:
            max_column = product
        index+=1

print(max_column)
#51,267,216
"""
"""
for c_index in range(20):
    diagonal_list = []
    for r_index in range(20):
        diagonal_list.append(grid[r_index][c_index])
    index = 0
    while index <= len(diagonal_list)-3:
        product = diagonal_list[index]*diagonal_list[index+1]*diagonal_list[index+2]*diagonal_list[index+3]
        if product > max_diagonal:
            max_diagonal = product
        index+=1
"""
     
        




