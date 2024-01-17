from game_data import data
from art import logo,vs
import random
import os

# print(logo)

gameActive = True
first_comparison = random.choice(data)
score = -1

def show_data (data, letter):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    print(f"Compare {letter}: {name}, a {description}, from {country}.")


def HigherOrLower(first_data, second_data):
    first_count = first_data['follower_count']
    second_count = second_data['follower_count']
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A" and first_count>second_count:
        print("You are Right")
        return True
    elif choice == "B" and first_count<second_count:
        print("You are Right")
        global first_comparison 
        first_comparison = second_comparison
        return True
    else:
        return False


while gameActive:
    score += 1 
    second_comparison = random.choice(data)
    if second_comparison == first_comparison:
        second_comparison = random.choice(data)
    print(first_comparison)
    print(second_comparison)

    show_data(first_comparison,"A")
    print(vs)
    show_data(second_comparison,"B")

    gameActive = HigherOrLower(first_comparison, second_comparison)
    os.system('cls')



print(f"You Lost, Your Socre is {score}")



# What if the 2 choices where the same
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}