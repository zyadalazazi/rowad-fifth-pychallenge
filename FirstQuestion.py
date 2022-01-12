# Initializing the integer total to 0
total = 0

"""
Continuing to add numbers until the sum is over 50,
while making sure the input is a number
"""
while total <= 50:
    num = input("Please enter a number to add:")

    while not num.isnumeric():
        num = input("Please input a number not a character:\nThe total so far is: {}".format(total))

    total += int(num)
    print("\nThe total is: {0}".format(total))

# Showing the user has exceeded the total limit
print("The total has reached its maximum value.")