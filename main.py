import random
def rolldice(min,max):
    while True:
        print("Rolling Dice...")
        number= random.randint(min,max)
        print(f"your number is: {number}")
        Choice = input("Do you want to roll the dice again? (Y/N)")
        if Choice.upper()=='N':
            break
rolldice(1,6)