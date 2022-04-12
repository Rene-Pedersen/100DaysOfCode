# Blind Auction Program
from Art import logo

def clear():
    # Due to running in PyCharm we don't have access to os clear function so we just add some blank lines
    print('\n'*80)


print(logo)
print("Welcome to the blind auction")

bidders = {}
more_bidders = "yes"

while more_bidders == "yes":
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    bidders[name] = bid
    more_bidders = input("Are there more bidders? yes/no ")
    clear()

winner = ""
max_bid = 0
for name in bidders:
    if bidders[name] > max_bid:
        winner = name
        max_bid = bidders[name]

print(f"The winner is {winner} with a bid of ${max_bid}")
