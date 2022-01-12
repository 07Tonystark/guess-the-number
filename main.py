import random


def guess(x):
    ran_num = random.randint(1, x)
    num = 0
    while num != ran_num:
        num = int(input(f"guess a number between 1 and {x}:"))
        if num > ran_num:
            print("Too high, Guess again")
        elif num < ran_num:
            print("Too low, Guess again")
    print(f"Congrats, Your guess {ran_num} is correct")


def cguess(x):
    low = 1
    high = x
    msg = ''
    while msg != 'c':
        if low != high:
            ran_num = random.randint(low, high)
        else:
            ran_num = high
        msg = input(f"Is {ran_num} High(h),Low(l) or Correct(c)??").lower()
        if msg == 'h':
            high = ran_num - 1
        elif msg == 'l':
            low = ran_num + 1
    print(f"Yay,Computer has guessed your number {ran_num} correctly!!")


difficulty = {'E': 100, 'M': 500, 'H': 1000}
print("Welcome, to the Number Guessing Game")
a = int(input("Press 0 if you want computer to guess your number, Press 1 if you want to guess the number:"))
b = input("enter the difficulty level (E),(M) or (H)")
if a == 0:
    cguess(difficulty[b])
elif a == 1:
    guess(difficulty[b])
