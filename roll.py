# roll a "die" some number of times.
import random

def dice(number_of_rolls):
    dice_rolls = []
    for _ in range(number_of_rolls):
        roll = random.randint(1, 6)
        dice_rolls.append(roll)
    return dice_rolls

# roll - run it once and go into a loop
print(dice(1))

# roll 1 - produce a number 1-6 random and print it
print(dice(1))
# roll 2 - produce two numbers 1-6 and print them
print(dice(2))
# roll 3 - produce three numbers and print them.
print(dice(3))

while True:
# ask user how many times they want to roll
    number_of_rolls = int(input("How many times do you want to roll the die? "))
    print(dice(number_of_rolls))  # print the results of the rolls
       
# ask user if they want to roll again
    user_input = input("Do you want to roll again? (yes/no): ")
    if user_input.lower() != 'yes':
        break

