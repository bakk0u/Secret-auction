import os
from art import logo
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print("Welcome to the secret auction program.")
bids_log = {}
choice = "yes" 
while choice == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids_log[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice == "yes":
        clear()

highest_bid = 0
winner = ""
for key in bids_log:
    if bids_log[key] >= highest_bid:
        highest_bid = bids_log[key]
        winner = key
    else:
        continue
print(f"The winner is {winner} with a bid of ${highest_bid} .")
