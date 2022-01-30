# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_count = 0
for i in "true":
    true_count += name1.lower().count(i) + name2.lower().count(i)

love_count = 0
for j in "love":
    love_count += name1.lower().count(j) + name2.lower().count(j)

score = int(str(true_count)+str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
