# Write your code below this line 👇
# import math
# def prime_checker(number):
#     if number > 2:
#         num_divisors = 0
#         for i in range(1, math.ceil(number/2)):
#             if number % i == 0:
#                 num_divisors += 1
#         if num_divisors > 1:
#             print("It's not a prime number.")
#         else:
#             print("It's a prime number.")
#     elif number == 2:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
         print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)