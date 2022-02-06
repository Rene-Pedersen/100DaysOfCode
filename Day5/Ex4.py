#Write your code below this row 👇
# FizzBuzz 1-100
# if divisible by 3 print "Fizz"
# if divisible by 5 print "Buzz"
# if divisible by both 3 and 5 print "FizzBuzz"
# if neither just print the number

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
