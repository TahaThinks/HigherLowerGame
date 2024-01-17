from game_data import data
from art import logo,vs
import random
import os

# print(logo)

gameActive = True



def HigherOrLower(first_count, second_count):
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A" and first_count>second_count:
        print("You are Right")
        return True
    elif choice == "B" and first_count<second_count:
        print("You are Right")
        return True
    else:
        print("You are Wrong")
        return False


while gameActive:
    first_comparison = random.choice(data)
    second_comparison = random.choice(data)
    print(first_comparison)
    print(second_comparison)

    print(f"Compare A: {first_comparison['name']}, a {first_comparison['description']}, from {first_comparison['country']}.")
    print(vs)
    print(f"Compare B: {second_comparison['name']}, a {second_comparison['description']}, from {second_comparison['country']}.")
    gameActive = HigherOrLower(first_comparison['follower_count'], second_comparison['follower_count'])
    os.system('cls')



print("This is the End")



# What if the 2 choices where the same
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}