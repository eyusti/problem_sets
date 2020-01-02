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
"""def smallest_multiple():
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

print(smallest_multiple())"""

# problem 6

"""sum_of_squares = 0
square_of_sums = 0

#sum of squares
for num in range (1,101):
    sum_of_squares += num**2

#square of sums
for num in range (1,101):
    square_of_sums += num

print((square_of_sums**2)-sum_of_squares)"""

# problem 7
"""list_of_primes = [2,3,5,7,11,13]
current_number = 15

def is_prime(test_num):
    for num in range(3,test_num):
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
import math
def special_pythagorean_triplet():
    for a in range(1,333):
        for b in range (a+1,500):
            c = math.sqrt(a**2+b**2)
            print(a)
            print(b)
            print(c)
            if a**2+b**2 == c**2 and b > a and c > b and a + b + c == 1000:
                return(a*b*c) 

print(special_pythagorean_triplet())
               




