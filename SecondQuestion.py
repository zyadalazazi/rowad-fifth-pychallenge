# Importing the random module
from random import randint


# A function that generates a random number between two numbers
def generate_number(start, end):
    if start <= end:
        comp_num = randint(start, end)
    else:
        comp_num = randint(end, start)

    return comp_num


# A function that checks if two numbers are equal
def check_guess(comp_num, user_guess):

    if user_guess < comp_num:
        print("Too low")
        return False
    elif user_guess > comp_num:
        print("Too high")
        return False
    else:
        print("Congratulations! Your guess is correct.")
        return True


# A function that asks the user for a number
def ask_number():

    print("I am thinking of a number...")
    user_guess = input("Can you tell what number I am thinking of:")

    return user_guess


# The start of the actual program
lower, higher = input("Please input the lower bound:"), input("Please input the higher bound:")

fl = False
while not fl:
    if lower.isnumeric() and higher.isnumeric():
        fl = True
    else:
        print("Please input numbers not characters")
        lower, higher = input("Please input the lower bound:"), input("Please input the higher bound:")

comp_num = generate_number(int(lower), int(higher))

user_guess = ask_number()
while not user_guess.isnumeric():
    print("Please enter a number")
    user_guess = ask_number()

while not check_guess(comp_num, int(user_guess)):
    user_guess = ask_number()
    print("User guess is:", user_guess)
else:
    print("You did a great job!")

