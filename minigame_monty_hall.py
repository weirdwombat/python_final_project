"""
Program : minigame_monty_hall.py
Author : Olivia Kennedy
Date Last Modified 08/02/2020
This program allows the user to provide input of their choice of door 1, 2, or 3 and their choice
of doors after the host reveals a door that is not the prize door or the one they picked
originally. This is modeled after the Monty Hall Problem.
"""
import random
print("There are 3 doors. Two of them have goats, but the last one has a car!")
user_input = int(input("Do you want to pick Door 1, 2, or 3: "))
prize_door = random.randrange(1,4)


doors = ['goat', 'goat', 'goat']

doors[prize_door-1] = 'car'

class InvalidDoorSelection(Exception):
    pass
    #user_input = input("Please enter the number of the door only. Do you want to pick  Door 1, 2, or 3: ")

def door_selection_1():
    if user_input not in [1,2,3]:
        raise InvalidDoorSelection
    else:
        print("input is valid")

def door_selection_2():
    if final_door not in [1,2,3]:
        raise InvalidDoorSelection
    else:
        print("input is valid")


def host_reveal():
    if(user_input != 1 and prize_door != 1):
        print('Host revealed a',doors[0],'in door 1')
    elif(user_input != 2 and prize_door != 2):
        print('Host revealed a',doors[1],'in door 2')
    elif(user_input != 3 and prize_door != 3):
        print('Host revealed a',doors[2],'in door 3')


def win_or_lose():
    if final_door == prize_door:
        return("You win a car!!!")
    else:
        return("You win a goat!!!")

if __name__ == '__main__':
    door_selection_1()
    host_reveal()
    final_door = int(input("This is your final guess. Do you want Door 1, 2, or 3: "))
    door_selection_2()
    print(win_or_lose())
    print("for debugging:",doors)




