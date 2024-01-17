from game_data import data
from art import logo,vs
import random
import os

# print(logo)

gameActive = True
first_comparison = random.choice(data)
score = -1

def show_data (name, desription, country, letter):
    print(f"Compare {letter}: {name}, a {desription}, from {country}.")


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
    print(first_comparison)
    print(second_comparison)

    show_data(first_comparison['name'],first_comparison['description'],first_comparison['country'],"A")
    print(vs)
    show_data(second_comparison['name'],second_comparison['description'],second_comparison['country'],"B")

    gameActive = HigherOrLower(first_comparison, second_comparison)
    os.system('cls')



print(f"You Lost, Your Socre is {score}")



# What if the 2 choices where the same
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}
# {'name': 'Drake', 'follower_count': 65, 'description': 'Musician', 'country': 'Canada'}